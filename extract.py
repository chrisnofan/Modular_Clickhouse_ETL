import pandas as pd

#function to get data
def fetch_data(client, query):
    '''
    fetches query results from a clickhouse database and writes to a csv file

    Parameters:
    - client(clickhouse_connect.Client)
    - query (A SQL select query)

    Returns: None
    '''

    #execute the qurey
    result = client.query(query)
    rows = result.result_rows
    cols = result.column_names

    #close the client
    client.close()

    #Write to pandas df and csv file
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv('tripdata.csv', index=False)

    print(f'{len(df)} rows Successfully extracted')


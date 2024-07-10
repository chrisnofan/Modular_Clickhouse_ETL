##importing custom functions

from helpers import get_client, get_postgress_engine
from extract import fetch_data
from load import load_csv_to_postgres
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


query = '''
        select pickup_date, vendor_id, passenger_count, trip_distance, payment_type, fare_amount, tip_amount 
        from tripdata
        where year(pickup_date) = 2015 and month(pickup_date) = 1 and dayOfMonth(pickup_date) = 8

        '''

client = get_client()
engine = get_postgress_engine()


def main():
    '''
    Main function to run the data pipeline modules
    1. ------
    2. -------

    Parameters: None

    Returns: None
    '''

    #Extract the data
    fetch_data(client=client, query=query)

    #load the data to the staging area
    load_csv_to_postgres('tripdata.csv', 'tripdata', engine, 'STG')

    ## execute stored procedure
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(text('CALL "STG".agg_tripdata()'))
    session.commit()
    
    print('Stored procedure executed')

    print('Pipeline executed successfully')


if __name__ == '__main__':
    main()



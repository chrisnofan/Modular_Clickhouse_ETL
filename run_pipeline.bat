@echo off

:: Define the logfile
set LOGFILE=pipeline_log.txt

:: Log the start time
echo Running pipeline at %date% %time% >> %LOGFILE%

:: Run the main.py and log the output

c:/Users/chris/Downloads/Tenalytics/ETL/Modular_Clickhouse_ETL/myvenv/Scripts/python.exe main.py >> %LOGFILE% 2>&1

:: log the end time
echo Pipeline completed at %date% %time% >> %LOGFILE%

echo. >> %LOGFILE%
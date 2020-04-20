# FDA RES Data Automated Cloud ETL 

For more info about this dataset see https://open.fda.gov/apis/food/enforcement  

- Pulled JSON data from a US gov website endpoint
- Saved it on Linux machine
- Converted the "results" part in a CSV dataframe
- Renamed the file as its timestamp
- Imported it in a AWS S3 bucket with Amazon Command Line Interface
- Automated the entire process with Airflow   

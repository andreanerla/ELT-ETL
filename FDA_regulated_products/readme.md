# FDA RES Data Automated Cloud ETL 

![Alt Text](https://i.imgur.com/PUJwTjV.png)



For more info about this dataset see https://open.fda.gov/apis/food/enforcement  

- Pulled JSON data from a US gov website endpoint
- Saved it in Linux environment
- Converted the "results" part in a CSV dataframe
- Renamed the file as its timestamp
- Imported it in a AWS S3 bucket with Amazon Command Line Interface
- Automated the entire process to run every Monday with a Airflow DAG   



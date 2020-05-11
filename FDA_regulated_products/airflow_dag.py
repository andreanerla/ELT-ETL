
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd
import json
import os
from datetime import datetime

def etl():
    r = requests.get('https://api.fda.gov/food/enforcement.json?limit=100') #pulling the first 100 rows from the website
    data = json.load(open("enforcement.json")) #opening the json file
    df = pd.DataFrame(data["results"]) #saving the json file as pandas dataframe
    df['openfda']= df['openfda'].astype(str) #without this step the "openfda" column would be treated as "dict" type
    now = datetime.now()
    now_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) 
    return os.system(r'aws s3 cp ./fda_csv.csv s3://fda-regulated-products/fda_' + now_date + '.csv') 

dag = DAG('fda_products', description='FDA products from US gov. endpoint to AWS S3 bucket',
           schedule_interval='0 0 * * MON',
          start_date=datetime(2020, 4, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries = 3, dag=dag)

fda_operator = PythonOperator(task_id='fda_etl_task', python_callable=etl, dag=dag)

dummy_operator >> fda_operator

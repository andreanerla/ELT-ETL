import requests
import pandas as pd
import json
import pyodbc
import os
from datetime import datetime

r = requests.get('https://api.fda.gov/food/enforcement.json?limit=100') #pulling the first 100 rows from the website endpoint (unfortunately I'm not allowed to pull more than 100 rows) 

data = open('enforcement.json', 'wb').write(r.content) # saving the json file locally

data = json.load(open("enforcement.json")) #opening the json file 

df = pd.DataFrame(data["results"]) #saving the json file as pandas dataframe

df['openfda']= df['openfda'].astype(str) #without this step the "openfda" column would be treated as "dict" type, causing the table to not be uploaded to SQL

csv_df = df.to_csv("fda_csv.csv") #converting the file as CSV

now = datetime.now()

now_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) #assigning the current date to the file which will be uploaded on S3

os.system(r'aws s3 cp C:\Users\andre\Documents\fda_csv.csv s3://fda-regulated-products/fda_' + now_date + '.csv') #uploading the file to S3 bucket with amazon command line interface




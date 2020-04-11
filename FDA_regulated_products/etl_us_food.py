'''
The openFDA food enforcement reports API returns data from the FDA Recall Enterprise System (RES),
a database that contains information on recall event information submitted to FDA.
Currently, this data covers publicly releasable records from 2004-present. The data is updated weekly.
The procedures followed to input recall information into RES when FDA learns of a recall event
are outlined in Chapter 7 of FDA’s Regulatory Procedure Manual The Regulatory Procedures Manual is a reference manual for FDA personnel.
It provides FDA personnel with information on internal procedures to be used in processing domestic and import regulatory and enforcement matters.
'''

import requests
import pandas as pd
import json
from sqlalchemy import create_engine
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




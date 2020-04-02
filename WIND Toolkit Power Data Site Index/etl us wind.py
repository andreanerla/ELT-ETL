import requests
import pandas as pd
from sqlalchemy import create_engine
import pyodbc

req = requests.get("https://data.nrel.gov/files/54/wtk_site_metadata.csv")

csv_data = open('us_wind.csv', 'wb').write(req.content) 

df = pd.read_csv('us_wind.csv')

engine = create_engine('mssql+pyodbc://LAPTOP-NAAAGCHR\SQLEXPRESS/DS udemy training?driver=SQL server?Trusted_Connection = yes')

conn = engine.connect()

tosql = df.to_sql('wind', con=engine,if_exists="append",index=False,chunksize=1000)


conn.close()

#todo
#normalize tables
#transformation da pandas o sql?

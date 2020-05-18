# WIND Toolkit Power Data ETL

![Alt Text](https://i.imgur.com/EeBYJh5.png)

![Alt Text](https://i.imgur.com/9dMrR1B.png)

- Extracted CSV file (127K rows) from https://data.nrel.gov/files/54/wtk_site_metadata.csv
- Converted it into Pandas dataframe and stored it in local SQL Server
- Reorganized the dataframe following a star schema organization with a SQL Stored Procedure
- Graphically represented the star schema

To do: 
- Normalize the tables
- Include "/" in full_timeseries_path

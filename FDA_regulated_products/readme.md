For more info about this dataset see https://open.fda.gov/apis/food/enforcement  

- Pulled JSON data from a US website endpoint
- Saved it locally
- Converted the "results" part in a CSV dataframe
- Renamed the file as the date (Y, M, D, H, M) in which it was downloaded
- Imported it in a AWS S3 bucket
- Automated the entire process to run every Monday with Task Scheduler 

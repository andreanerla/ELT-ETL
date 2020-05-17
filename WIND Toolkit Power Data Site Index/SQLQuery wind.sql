
SELECT site_id, longitude, latitude, state, county, fraction_of_usable_area
INTO [DS udemy training].[dbo].[wind_geography]
FROM [DS udemy training].[dbo].[wind];
 
---

SELECT site_id, full_timeseries_directory, right(full_timeseries_path, len(full_timeseries_path)-1) as full_timeseries_path  
INTO [DS udemy training].[dbo].[wind_dir_path]
FROM [DS udemy training].[dbo].[wind];

'''
deleting the first charachter of full_timeseries_path as it is redundant (already present in full_timeseries_directory)
'''
---

ALTER TABLE [DS udemy training].[dbo].[wind] 
DROP COLUMN longitude, latitude, state, county, full_timeseries_directory, full_timeseries_path, fraction_of_usable_area




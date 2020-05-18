USE [DS udemy training];
GO

ALTER PROC sp_wind
AS
BEGIN
	DROP TABLE wind_dir_path, wind_geography

	SELECT site_id, longitude, latitude, state, county, fraction_of_usable_area
	INTO [DS udemy training].[dbo].[wind_geography]
	FROM [DS udemy training].[dbo].[wind];
	---
	SELECT site_id, full_timeseries_directory, full_timeseries_path  
	INTO [DS udemy training].[dbo].[wind_dir_path]
	FROM [DS udemy training].[dbo].[wind];

	UPDATE wind_dir_path
	SET full_timeseries_path = RIGHT(full_timeseries_path, len(full_timeseries_path) - CHARINDEX('/', full_timeseries_path))
	---
	ALTER TABLE [DS udemy training].[dbo].[wind] 
	DROP COLUMN longitude, latitude, state, county, full_timeseries_directory, full_timeseries_path, fraction_of_usable_area
END
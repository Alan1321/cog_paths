from sqlite_db_db import sqlitedbb

from TRMM_LIS import add_trmmlis_path
from OTD import add_otd_path
from ISS_LIS import add_isslis_path

from dotenv import load_dotenv
import os

##LOAD_ENV_VARIABLES
print("Loading env variables...." , end='')
load_dotenv()
TRMM_LIS_S3_PATH=os.getenv('TRMM_LIS_BASE_PATH')
OTD_S3_PATH=os.getenv('OTD_BASE_PATH')
ISS_LIS_S3_PATH=os.getenv('ISS_LIS_SPRING2023_BASE_PATH')
print("Complete")

##DECLARE_INITIALIZE 
print("Initializing variables....", end='')
driver_name = "raster2.sqlite"
rasters = {}
print("Complete")

##ADD_TO_RASTER_DICTIONARY_HERE
print("Creating Raster Dictionary....", end='')
TRMM_LIS = add_trmmlis_path(rasters, TRMM_LIS_S3_PATH)
OTD = add_otd_path(rasters, OTD_S3_PATH)
ISS_LIS = add_isslis_path(rasters, ISS_LIS_S3_PATH)
print("Complete")

##ADD_PATH_TO_SQLITE_DB_HERE
print("Adding paths to sqlitedb....", end='')
driver = sqlitedbb(driver_name, rasters)
driver.make_new_db()
print("Complete")

##PRITN_DRIVER_HERE
driver.print()



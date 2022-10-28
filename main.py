from sqlite_db_db import sqlitedbb

from TRMM_LIS import add_trmmlis_path
from OTD import add_otd_path
from ISS_LIS import add_isslis_path

from dotenv import load_dotenv
import os

load_dotenv()
TRMM_LIS_S3_PATH=os.getenv('TRMM_LIS_BASE_PATH')
OTD_S3_PATH=os.getenv('OTD_BASE_PATH')
ISS_LIS_S3_PATH=os.getenv('ISS_LIS_SPRING2023_BASE_PATH')

driver_name = "raster2.sqlite"
rasters = {}

print("Step 1 Complete!!")
############################################MAKE_RASTERS_HERE##########################################################################################

TRMM_LIS = add_trmmlis_path(rasters, TRMM_LIS_S3_PATH)
OTD = add_otd_path(rasters, OTD_S3_PATH)
ISS_LIS = add_isslis_path(rasters, ISS_LIS_S3_PATH)

print("Step 2 Complete!!")
#############################################ADD_PATH_TO_SQLITE_DB_HERE################################################################################
driver = sqlitedbb(driver_name, rasters)
driver.make_new_db()

print("Step 3 Complete!!")
##############################################PRITN_DRIVER_HERE########################################################################################
driver.print()
#######################################################################################################################################################

from TRMM_LIS import add_trmmlis_path
from OTD import add_otd_path
from ISS_LIS import add_isslis_path
from sqlite_db_db import sqlitedbb

driver_name = "raster2.sqlite"
rasters = {}

print("Step 1 Complete!!")
############################################MAKE_RASTERS_HERE##########################################################################################

TRMM_LIS = add_trmmlis_path(rasters)
OTD = add_otd_path(rasters)
ISS_LIS = add_isslis_path(rasters)

print("Step 2 Complete!!")
#############################################ADD_PATH_TO_SQLITE_DB_HERE################################################################################
driver = sqlitedbb(driver_name, rasters)
driver.make_new_db()

print("Step 3 Complete!!")
##############################################PRITN_DRIVER_HERE########################################################################################
driver.print()
#######################################################################################################################################################

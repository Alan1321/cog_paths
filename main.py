import terracotta as tc
from TRMM_LIS import add_trmmlis_path
from OTD import add_otd_path
from ISS_LIS import add_isslis_path


driver_name = "raster_test.sqlite"

# driver = tc.get_driver('raster_test.sqlite')
# key_names = ('type', 'date', 'band')
# driver.create(key_names)

rasters = {}

print("Step 1 Complete!!")
############################################ADD_PATH_TO_RASTERS_HERE###################################################################################

TRMM_LIS = add_trmmlis_path(rasters)
OTD = add_otd_path(rasters)
ISS_LIS = add_isslis_path(rasters)

print("Step 2 Complete!!")
#############################################ADD_PATH_TO_SQLITE_DB_HERE################################################################################

# i = 0
# for keys, raster_file in rasters.items():
#     driver.insert(keys, raster_file)
#     i = i+1

print("Step 3 Complete!!")
#######################################################################################################################################################

# for i,j in driver.get_datasets().items():
#     print(i,j)
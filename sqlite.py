import terracotta as tc
from TRMM_LIS import add_trmmlis_path
from OTD import add_otd_path
from ISS_LIS import add_isslis_path

class sqlite():
    def __init__(self, driver_name,rasters):
        self.driver_name = driver_name
        self.rasters = rasters
        self.driver = None
    
    def make_new_db(self):
        self.driver = tc.get_driver(self.driver_name)
        key_names = ('type', 'date', 'band')
        self.driver.create(key_names)

        for keys, raster_file in self.rasters.items():
            self.driver.insert(keys, raster_file)

    def append_to_db(self):
        self.driver = tc.get_driver(self.driver_name)
        for keys, raster_file in self.rasters.items():
            self.driver.insert(keys, raster_file)

    def print_db(self):
        for i,j in self.driver.get_datasets().items():
            print(i,j)

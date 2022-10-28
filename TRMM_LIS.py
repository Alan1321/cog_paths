class add_trmmlis_path:
    def __init__(self, rasters, base_path):
        self.rasters = rasters
        self.path = base_path
        self.add_trmm_full()
        self.add_trmm_seasonal()
        self.add_trmm_monthly()
        self.add_trmm_diurnal()
        self.add_trmm_daily()

    def add_trmm_full(self):
        self.rasters[('VHRFC','201301','LIS')] = f'{self.path}/VHRFC_LIS_FRD_co.tif'
    
    def add_trmm_seasonal(self):
        self.rasters[('VHRSC','2013_03_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_1.0_co.tif'
        self.rasters[('VHRSC','2013_07_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_2.0_co.tif'
        self.rasters[('VHRSC','2013_10_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_3.0_co.tif'
        self.rasters[('VHRSC','2013_12_01','LIS')] = f'{self.path}/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_4.0_co.tif'
    
    def add_trmm_monthly(self):
        for i in range(9):
            self.rasters[('VHRMC',f'20130{i+1}','LIS')] = f'{self.path}/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+1}.0_co.tif'

        for i in range(3):
            self.rasters[('VHRMC',f'2013{i+10}','LIS')] = f'{self.path}/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+10}.0_co.tif'

    def add_trmm_diurnal(self):
        a = '01'
        b = '15'
        count = 0

        for i in range(9):
            self.rasters[('VHRDC',f'2013_0{i+1}_01','LIS')] = f'{self.path}/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
            count+=1
            self.rasters[('VHRDC',f'2013_0{i+1}_15','LIS')] = f'{self.path}/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
            count+=1

        for i in range(3):
            self.rasters[('VHRDC',f'2013_{i+10}_01','LIS')] = f'{self.path}/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
            count+=1
            self.rasters[('VHRDC',f'2013_{i+10}_15','LIS')] = f'{self.path}/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
            count+=1
    
    def add_trmm_daily(self):
        calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        count = 1

        for x in range(12):
            month = '00'
            if(x+1 <= 9):
                month = f'0{x+1}'
            else:
                month = f'{x+1}'

            for i in range(calendar[x]): 
                if i+1 <= 9:
                    self.rasters[('VHRAC',f'2013_{month}_0{i+1}','LIS')] = f'{self.path}/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
                else:
                    self.rasters[('VHRAC',f'2013_{month}_{i+1}','LIS')] = f'{self.path}/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
                count+=1

    def get_raster(self):
        return self.rasters
class add_otd_path:
    def __init__(self, rasters, base_path):
        self.rasters = rasters
        self.path = base_path
        self.add_otd_full()
        self.add_otd_monthly()
        self.add_otd_diurnal()
        self.add_otd_daily()

    def add_otd_full(self):
        self.rasters[('HRFC', '201301', 'OTD')] = f'{self.path}/HRFC_COM_FR_co.tif'
    
    def add_otd_monthly(self):
        for i in range(12):
            month = '00'
            if(i+1 <= 9):
                month = f'0{i+1}'
            else:
                month = f'{i+1}'
            self.rasters[('HRMC', f'2013{month}', 'OTD')] = f'{self.path}/HRMC_COM_FR_cogs/HRMC_COM_FR_Month_{i+1}.0_co.tif'
    
    def add_otd_diurnal(self):
            count = 0

            for i in range(12):
                month = '00'
                if(i+1 <= 9):
                    month = f'0{i+1}'
                else:
                    month = f'{i+1}'
                self.rasters['LRDC',f'2013_{month}_01','OTD'] = f'{self.path}/LRDC_COM_FR_cogs/LRDC_COM_FR_Local_Hour_{count}.5_co.tif'
                count+=1
                self.rasters['LRDC',f'2013_{month}_15','OTD'] = f'{self.path}/LRDC_COM_FR_cogs/LRDC_COM_FR_Local_Hour_{count}.5_co.tif'
                count+=1

    def add_otd_daily(self):
            calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            count = 0

            for x in range(12):
                month = '00'
                if(x+1 <= 9):
                    month = f'0{x+1}'
                else:
                    month = f'{x+1}'

                for i in range(calendar[x]): 
                    if i+1 <= 9:
                        self.rasters[('HRAC',f'2013_{month}_0{i+1}','OTD')] = f'{self.path}/HRAC_COM_FR_cogs/HRAC_COM_FR_Day_of_year_{count}.0_co.tif'
                    else:
                        self.rasters[('HRAC',f'2013_{month}_{i+1}','OTD')] = f'{self.path}/HRAC_COM_FR_cogs/HRAC_COM_FR_Day_of_year_{count}.0_co.tif'
                    count+=1

    def get_raster(self):
        return self.rasters
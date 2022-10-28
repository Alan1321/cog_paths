import terracotta as tc
import json

driver = tc.get_driver('raster2.sqlite')
key_names = ('type', 'date', 'band')
driver.create(key_names)

rasters = {

}

####################################################TRMM_LIS_FULL########################################################################################

rasters[('VHRFC','201301','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRFC_LIS_FRD_co.tif'

#####################################################TRMM_LIS_SEASONAL###################################################################################

rasters[('VHRSC','2013_03_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_1.0_co.tif'
rasters[('VHRSC','2013_07_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_2.0_co.tif'
rasters[('VHRSC','2013_10_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_3.0_co.tif'
rasters[('VHRSC','2013_12_01','LIS')] = 's3://ghrc-cog/TRMM-LIS/VHRSC_LIS_FRD_cogs/VHRSC_LIS_FRD_Season_4.0_co.tif'

######################################################TRMM_LIS_MONTHLY###################################################################################

for i in range(9):
    rasters[('VHRMC',f'20130{i+1}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+1}.0_co.tif'

for i in range(3):
    rasters[('VHRMC',f'2013{i+10}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRMC_LIS_FRD_cogs/VHRMC_LIS_FRD_Month_{i+10}.0_co.tif'

#######################################################TRMM_LIS_DIURNAL####################################################################################
a = '01'
b = '15'
count = 0

for i in range(9):
    rasters[('VHRDC',f'2013_0{i+1}_01','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1
    rasters[('VHRDC',f'2013_0{i+1}_15','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1

for i in range(3):
    rasters[('VHRDC',f'2013_{i+10}_01','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1
    rasters[('VHRDC',f'2013_{i+10}_15','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRDC_LIS_FRD_cogs/VHRDC_LIS_FRD_Time_{count}.0_co.tif'
    count+=1

#######################################################TRMM_LIS_DAILY#####################################################################################
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
            rasters[('VHRAC',f'2013_{month}_0{i+1}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
        else:
            rasters[('VHRAC',f'2013_{month}_{i+1}','LIS')] = f's3://ghrc-cog/TRMM-LIS/VHRAC_LIS_FRD_cogs/VHRAC_LIS_FRD_Time_{count}.0_co.tif'
        count+=1

###########################################################OTD_FULL######################################################################################################

rasters[('HRFC', '201301', 'OTD')] = 's3://ghrc-cog/OTD/HRFC_COM_FR_co.tif'

############################################################OTD_MONTHLY##################################################################################################

for i in range(12):
    month = '00'
    if(i+1 <= 9):
        month = f'0{i+1}'
    else:
        month = f'{i+1}'
    rasters[('HRMC', f'2013{month}', 'OTD')] = f's3://ghrc-cog/OTD/HRMC_COM_FR_cogs/HRMC_COM_FR_Month_{i+1}.0_co.tif'

###############################################################OTD_DIURNAL###############################################################################################

count = 0

for i in range(12):
    month = '00'
    if(i+1 <= 9):
        month = f'0{i+1}'
    else:
        month = f'{i+1}'
    rasters['LRDC',f'2013_{month}_01','OTD'] = f's3://ghrc-cog/OTD/LRDC_COM_FR_cogs/LRDC_COM_FR_Local_Hour_{count}.5_co.tif'
    count+=1
    rasters['LRDC',f'2013_{month}_15','OTD'] = f's3://ghrc-cog/OTD/LRDC_COM_FR_cogs/LRDC_COM_FR_Local_Hour_{count}.5_co.tif'
    count+=1

###################################################################OTD_DAILY#############################################################################################

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
            rasters[('HRAC',f'2013_{month}_0{i+1}','OTD')] = f's3://ghrc-cog/OTD/HRAC_COM_FR_cogs/HRAC_COM_FR_Day_of_year_{count}.0_co.tif'
        else:
            rasters[('HRAC',f'2013_{month}_{i+1}','OTD')] = f's3://ghrc-cog/OTD/HRAC_COM_FR_cogs/HRAC_COM_FR_Day_of_year_{count}.0_co.tif'
        count+=1

######################################################ISS_LIS_Spring_2022################################################################################################
file = open('iss_lis_endpoints.json')
datasets = json.load(file)

for data in datasets:
    day_indices = data['day_indices']
    month = data['month']
    file = data['file']
    for key in day_indices:
        index1 = day_indices[key][0]
        index2 = day_indices[key][1]
        loop_len = index2 - index1 + 1
        date = key
        for i in range(loop_len):
            filename = file[index1]
            time = filename[25:31]
            index1 = index1 + 1
            rasters[('ISS_LIS',f'2022{month}{date}', f'{time}')] = f"s3://ghrc-cog/ISS_LIS/Spring2023/ISS_LIS_SC_V2.1_2022{month}{date}_{time}_NQC.tif"

######################################################ADD_ALL_TO_DRIVER##################################################################################################
i = 0

for keys, raster_file in rasters.items():
    driver.insert(keys, raster_file)
    i = i+1

#########################################################################################################################################################################
for i,j in driver.get_datasets().items():
    print(i,j)
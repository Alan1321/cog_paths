import sys
import json

class add_isslis_path:
    def __init__(self, rasters):
        self.rasters = rasters
        self.add_spring2022()
        
    def add_spring2022(self):
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
                    self.rasters[('ISS_LIS',f'2022{month}{date}', f'{time}')] = f"s3://ghrc-cog/ISS_LIS/Spring2023/ISS_LIS_SC_V2.1_2022{month}{date}_{time}_NQC.tif"        
    
    def get_raster(self):
        return self.rasters
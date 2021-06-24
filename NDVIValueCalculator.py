import csv

import numpy
import rasterio

path1=r'C:\Users\hafsa\Desktop\academics\8th semester\FYP II\Datasets\Farm 3\LandSAT 7\LE07_L2SP_151040_20050721_20200914_02_T1\LE07_L2SP_151040_20050721_20200914_02_T1_SR_B4.TIF'
path2=r'C:\Users\hafsa\Desktop\academics\8th semester\FYP II\Datasets\Farm 3\LandSAT 7\LE07_L2SP_151040_20050721_20200914_02_T1\LE07_L2SP_151040_20050721_20200914_02_T1_SR_B3.TIF'
band3=rasterio.open(path2)
band4=rasterio.open(path1)
band3=band3.read(1).flatten()
band4=band4.read(1).flatten()
ndvi=[]
#reads bands 4 and 3 as 0s
for x in band3:
    if ((band3[x]!=0)):
        print(band3[x])



print(ndvi)
print(len(ndvi))
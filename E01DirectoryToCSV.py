import pandas
import rasterio
import skimage.segmentation
from PIL import Image
import numpy as np
import sys
import os
import csv

# preparing a list of all hyperspectral band files
def createFileList(myDir, format='.TIF'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# loading all the bands of the hyperspectral image
myFileList = createFileList(r'C:\Users\hafsa\Desktop\academics\8th semester\FYP II\Datasets\Farm 3\EO-1\EO1H1510402005209110KF')
count = 0

# 3D matrix representing hypercube
img_file = np.zeros((3351,1031,108))
for file in myFileList:
    print(file)
    dataset = rasterio.open(file)
    img_file[:,:,count] = dataset.read(1)
    count+=1
    #df = img_file.flatten()

    #with open("Farm3HyperionDataset(1).csv", 'a',newline='') as f:
        #writer = csv.writer(f)
        #writer.writerow(df)

# SLIC Segmentation for the creation of super pixels
segments = skimage.segmentation.slic(img_file, n_segments=100, compactness=10.0, max_iter=10, sigma=0, spacing=None, multichannel=True, convert2lab=None, enforce_connectivity=True, min_size_factor=0.5, max_size_factor=3, slic_zero=False, start_label=None, mask=None)
print(segments);

# finding pixel count for each super pixel
pixelCount=[]
for x in range(len(np.unique(segments))):
    pixelCount.append(np.count_nonzero(segments == x))

# A 2D matrix with each row representing the mean reflectance value for each super pixel across the 108 bands
segmentedImage=np.zeros((len(np.unique(segments)),108))

# Computing Mean Reflectances for Superpixels
for x in range(3351):  # sum
    for y in range(1031):
        segmentedImage[segments[x,y],:] = segmentedImage[segments[x,y],:] + img_file[x,y,:];

for x in range(len(np.unique(segments))):  # division
    segmentedImage[x,:] = segmentedImage[x,:] / pixelCount[x];

print(segmentedImage)
print(segmentedImage.shape)
np.savetxt('segmentedImage.csv', segmentedImage, delimiter=',')






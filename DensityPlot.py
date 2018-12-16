from matplotlib import pyplot as plt
import csv
from scipy.stats import kde
import numpy as np

#ensure the str file is located in the same folder as the this script file.
str = 'Week 12 Trial Runs.csv'

counter = -1
x = []
y = []
with open(str) as csvDataFile:

    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        counter = counter + 1
        if counter > 0:
            x.append(float(row[0]))
            y.append(float(row[1]))



min = -5
max = 5

#change nbins to whatever you want. Higher number smoothes out the image
nbins = 100
k = kde.gaussian_kde([x,y])
xi, yi = np.mgrid[min:max:nbins*1j, min:max:nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
plt.colorbar()
plt.xlim(min,max)
plt.ylim(min,max)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Heat Map Week 12')
plt.show()

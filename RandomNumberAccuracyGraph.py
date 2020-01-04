###import numpy as np
import random as rand
import matplotlib.pyplot as plt

def getKeysAsList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list


numIter = 100
maxVal = 20
minVal = 1

values = dict()

#initialize dictionary values
for i in range(minVal, maxVal+1, 1):
    values[i] = 0

for i in range(numIter):
    values[rand.randint(minVal,maxVal)] += 1

xVals = getKeysAsList(values)


yVals = []
for key in xVals:
    yVals.append(values[key])

plt.bar(xVals, yVals, tick_label = xVals,
        width = 0.8, color = ['blue', 'green', 'purple'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('{} trials from {} to {}'.format(numIter, minVal, maxVal))

# function to show the plot
plt.show()

# print(values)
# print(xVals + yVals)
# print(rand.randint(0, 10))

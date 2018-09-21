import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataframe = pd.read_excel('D:\Downloads\\5_1.xls')

x=dataframe.X
y=dataframe.Y

#mean value of x and y
meanOfX = sum(x)/len(x)
meanOfy = sum(y)/len(y)

#calculating slope
slope = np.sum((x - meanOfX)*(y - meanOfy))/np.sum(np.square(x-meanOfX))
#calculating intercept
intercept = meanOfy - (slope * meanOfX)
#y output
yOutput = (slope * x) + intercept
plt.scatter(x,y)
plt.plot(x,y,"ro")  # plotting the line made by linear regression
plt.plot(x, yOutput)
plt.xlabel("X:national unemployment rate for adult males",fontsize=10)
plt.ylabel("Y:national unemployment rate for adult females",fontsize=10)
plt.show()

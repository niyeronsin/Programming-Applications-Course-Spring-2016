#import numpy and matlibplots module


#generate array of x values from 0 to 6pi

#calculate y values for sin wave

#calculate y values for cosine wave

#plot x and y values for both functions 

#set dashed line for sine wave and solide line for cosine wave

#add legend


#leave comment here with your information
#Name:
#Date:

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

x = np.linspace(0,6*pi,1000)

y_sin = sin(x)

y_cos = cos(x)

line1, = plt.plot(x, y_sin, '--', linewidth=2)
dashes = [10, 5, 20, 5]  # 10 points on, 5 off, 100 on, 5 off
line1.set_dashes(dashes)

line2, = plt.plot(x, y_cos, '-', linewidth=2)

plt.legend(('sin(x)','cos(x)'))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Homework 1')
plt.show()

#Name: Olaniyi Nafiu
#ID: 02765881
#Date: 1/19/2016

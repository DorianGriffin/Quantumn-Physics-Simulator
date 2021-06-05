# with higher pressure/temperature comes higer particle acceleration
#
import matplotlib.pyplot as plt
import numpy as np
import scipy
 # import pandas
import pygame
import tensorflow
import pip
# pip.main(['install','seaborn'])
Gas_constant = 8.3145 
temp = 220
n = 500
volume = np.array(range(10))
#will read a csv file with volume, temperatutre, gas constant, number of moles
#def test_func(volume, temp, n):
P = (n * (Gas_constant * 0.01) * temp)/(volume)
plt.plot(volume,P)
plt.title('Relationship between Volume and Pressure')
plt.xlabel('x Axis: Volume')
plt.ylabel('y Axis: Pressure')
plt.grid(alpha=.4,linestyle='-- ')
plt.show()
    #print(P)
    #calculate the wave propogation based upon the pressure of a given volume; we will visualize it

#testing the gas pressure equation, super basic


#test_func(np.array(range(10000)), 220, 500)















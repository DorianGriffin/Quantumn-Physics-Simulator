import matplotlib.pyplot as plt
import numpy as np
import math

Fs = 4000
f = 9#frequency 
sample = 1000
x = np.arange(sample) #the x axis range, in this case 0 to 1000
y = np.sin(9 * np.pi * f * x / Fs) #the equation
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()
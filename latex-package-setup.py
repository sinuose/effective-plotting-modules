'''
Author: Martin Jasinski
Purpose: Use Latex in matplotlib

Source: https://stackoverflow.com/questions/11367736/matplotlib-consistent-font-using-latex
'''
# for test purposes
import numpy as np

import matplotlib.pyplot as plt
import matplotlib

# initialize LateX engine
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.pyplot.title(r'ABC123 vs $\mathrm{ABC123}^{123}$')

# test function
def f(x):
  return np.cos(x) + 1/x^2

# plotting
plt.figure()
plt.title(r"plot of $cos(x) + \frac{1}{x^2}$)
plt.xlabel("X axis")
plt.ylabel("Y axis")
          
x_vals = np.linspace(0, 2 * np.pi, num=100)
plt.plot(x_vals, f(x_vals))
          
plt.show()


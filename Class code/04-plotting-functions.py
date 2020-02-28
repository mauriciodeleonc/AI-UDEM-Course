""" plotting-functions.py
    This Python script shows how you visualise data
    and plot functions using matplotlib.

    Author: Andres Hernandez G.
    Email: andres.hernandezg@udem.edu
    Institution: Universidad de Monterrey
    First created: Sun 26 Jan, 2020
"""

grades = [100, 90, 84, 87, 100, 85, 84, 98, 56, 89]

import matplotlib.pyplot as plt

plt.plot(grades, linewidth=3, color='red')
plt.xlabel('k-th student')
plt.ylabel('grade')
plt.title('Final grades')
plt.grid(True)

plt.figure(2)
plt.plot(grades, 'ok')
plt.xlabel('k-th student')
plt.ylabel('grades')
plt.title(r'Final grades with $\mu$=?', fontsize=20)
plt.grid()

plt.figure(3)
plt.hist(grades)

import numpy as np
grades_average = np.mean(grades)
print(grades_average)

plt.figure(4)
plt.plot(grades)
plt.xlabel('k-th student')
plt.ylabel('grades')
plt.title(r'Final grades with $\mu$={}'.
          format(grades_average), fontsize=20)
plt.grid()


theta = np.linspace(start=0, stop=2*3.141516, num=100)
y = np.sin(theta)
plt.figure(5)
plt.plot(theta, y, linewidth=3)
plt.grid(True)

import math
theta1 = np.arange(0, 2*math.pi, 0.1)

y = np.sin(theta1)
plt.figure(6)
plt.plot(theta1, y, linewidth=3)
plt.grid(True)

plt.show()




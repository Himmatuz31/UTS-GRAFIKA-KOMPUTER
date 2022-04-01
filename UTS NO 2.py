'''
Nama   : Himmatuz Zahiroh
NIM    : 20051397070
Kelas  : 2020B
'''
import numpy as np
import matplotlib.pyplot as plt
import random

n = 100
x = np.random.standard_normal(n)
y = 3.0 * x

fig = plt.subplots(figsize = (8, 4))

plt.hist2d(x,y)
plt.title("Simple 2D Histogram")

plt.show()


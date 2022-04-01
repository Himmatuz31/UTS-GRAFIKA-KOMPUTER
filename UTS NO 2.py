'''
Nama   : Himmatuz Zahiroh
NIM    : 20051397070
Kelas  : 2020B
Algoritma Kurva Bazier
'''

import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

Path = mpath.Path

fig, ax = plt.subplots()
pp1 = mpatches.PathPatch(
    Path([(0, 0), (0, 4), (4, 4), (0, 0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
    fc="none", transform=ax.transData)

ax.add_patch(pp1)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Titik merah harus berada pada path')

plt.show()

from matplotlib import pyplot as plt
from matplotlib import style

from numpy import genfromtxt

data = genfromtxt('ffd.tsv',delimiter=' ')

plt.plot(data)

plt.title('M¶/Ms')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

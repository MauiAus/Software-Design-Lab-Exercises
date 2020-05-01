#Made By Marielle Gabriel

import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1.5, 10)
plt.plot(x, x, label='linear', color='blue', linestyle='dashed')
plt.plot(x, x**2, label='quadratic', linestyle='solid')
plt.plot(x, x**3, 'rx', label='cubic')
plt.annotate('intersection', (1,1))
plt.xlim(-5,10)
plt.ylim(-5,10)
plt.grid(True)
locs, labels = plt.xticks()
plt.setp(labels, rotation=45)
plt.yticks(range(20, 100, 10) )
plt.grid(color = 'lightgrey', linestyle = '--', linewidth = .5)
plt.xlabel('x value')
plt.ylabel('y value')
plt.title("Simple Plot")
plt.legend()
plt.show()
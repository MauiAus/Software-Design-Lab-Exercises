import matplotlib.pyplot as plt

x_axis = ['vanilla','chocolate','strawbery','mint']
y_axis = [30,43,23,4]

plt.scatter(x_axis,y_axis, marker='x')
plt.ylim(0,45)
plt.grid(True)
plt.xlabel('ice-cream type')
plt.ylabel('pieces sold')
plt.title('ice-cream count')
plt.show()
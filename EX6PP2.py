import matplotlib.pyplot as plt

def cubic(x):
    return (x**3) + (53*(x**2)) - (400*x) + 25

x = []
y = []
for i in range(-30,31):
    x.append(i)
    y.append(cubic(i))

plt.plot(x,y, marker='.')
plt.grid(True)
plt.title('cubic polynomial')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Import the necessary libraries
x = np.arange(0, 5 * np.pi, 0.1)
y = np.sin(x)
y2 = x

x3 = np.arange(0, 5 * np.pi, 0.1)
y3 = np.cos(x3)

# Step 2: Plot the sine graph
plt.plot(x, y, color='green')
plt.plot(x3, y3, color='red')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Curve using Matplotlib')
plt.grid()

plt.savefig('1.png')

plt.show()

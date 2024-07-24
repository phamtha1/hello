import numpy as np
import matplotlib.pyplot as plt

# Step 1: Import the necessary libraries
x = np.arange(0, 5 * np.pi, 0.1)
y = np.sin(x)
y2 = x

# Step 2: Plot the sine graph
plt.plot(x, y, color='green')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Curve using Matplotlib')
plt.grid()

plt.savefig('1.png')

plt.show()

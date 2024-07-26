import numpy as np
import matplotlib.pyplot as plt

# Step 1: Import the necessary libraries
# tangent func for test2
x = np.arange(0, 5 * np.pi, 0.1)
y = np.tan(x)
y2 = x

# Step 2: Plot the sine graph
plt.plot(x, y, color='green')
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.title('Tangent Curve using Matplotlib')
plt.grid()

plt.savefig('2.png')

plt.show()
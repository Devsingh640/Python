import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100).reshape(10,10)

plt.title('TEST PLOT')
plt.ylabel('Y - Axis')
plt.xlabel('X - Axis')

plt.imshow(x, cmap = 'RdYlGn')
plt.colorbar()





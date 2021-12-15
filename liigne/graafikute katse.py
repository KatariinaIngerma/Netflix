import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle("sarjad ja filmid")
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
ax1.plot(x,y)
ax2.plot(x,-y)
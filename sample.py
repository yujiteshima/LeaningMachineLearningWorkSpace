# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
def sin(x: np.array) -> np.array:
  return np.sin(x)


x = np.arange(0, 2.0 * np.pi, 0.1)
plt.plot(x, sin(x))

# %%

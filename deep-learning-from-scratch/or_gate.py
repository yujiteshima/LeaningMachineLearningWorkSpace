# %%
import numpy as np


def OR(x1: int, x2: int):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1


# %%
OR(0, 0)
# %%
OR(1, 0)
# %%
OR(0, 1)
# %%
OR(1, 1)

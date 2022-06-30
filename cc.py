import numpy as np

a = np.zeros((9, 9), dtype=tuple)

a[1][2] = (1, 1, 11)
print(a)

import numpy as np
import math

thet = math.pi
thet = thet
n = 8
a = np.eye(8, dtype=complex)
b = np.complex(math.cos(thet), math.sin(thet))
row, col = np.diag_indices_from(a)
a[row, col] = b
c = np.random.normal(0, 1, (n, n))
print(c)
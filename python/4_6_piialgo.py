#myöhemmin

import random
import math


#
n = 0
N = 100000000000
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        n = n + 1
    print(f"Working...{i}")
    i =  i + 1

pii = (4 * n ) /  N
print(pii)
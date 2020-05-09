#!/usr/bin/env python3
import numpy as np
 
n, k = map(int, input().split())
p = list(map(int, input().split()))

E = lambda x: (x + 1) / 2
p = [E(p_) for p_ in p]
q = [0] + list(np.cumsum(p))
sum_ = [q[i+k] - q[i] for i in range(n-k+1)]

print(max(sum_))

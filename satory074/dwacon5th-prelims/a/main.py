import numpy as np

N = int(input())
a = list(map(int, input().split()))

avg = sum(a) / len(a)
diff_a = [abs(avg - a_) for a_ in a]
print(np.argmin(diff_a))


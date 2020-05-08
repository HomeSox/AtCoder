import itertools
import math
N = int(input())
xy = []
for i in range(N):
    a, b = map(int, input().split())
    xy.append([a,b])

s = 0

waru = math.factorial(N)
for v in itertools.permutations(xy, N):
    for i in range(len(v)-1):
        s += math.sqrt(pow(v[i][0]-v[i+1][0],2) + pow(v[i][1]-v[i+1][1],2))
print(float(s)/waru)

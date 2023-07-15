import collections as cl
import math

E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))

cnt = 0
for l in L:
    if l in E:
        cnt += 1

if cnt == 6:
    print(1)
elif cnt == 5:
    if B in L:
        print(2)
    else:
        print(3)
elif cnt == 4:
    print(4)
elif cnt == 3:
    print(5)
else:
    print(0)

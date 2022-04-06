import collections as cl

N = int(input())
a = list(map(int, input().split()))

clc = cl.Counter(a)

if len(clc) == 1:
    print("Yes" if clc[0] == N else "No")
elif len(clc) == 2:
    print("Yes" if clc[0] == N // 3 else "No")
elif len(clc) == 3:
    x, y, z = clc.keys()
    print("Yes" if x ^ y ^ z == 0 and clc[x] == clc[y] == clc[z] else "No")
else:
    print("No")


import collections as cl
import math

M = int(input())

S1 = list(input())
S1 *= 5
S2 = list(input())
S2 *= 5
S3 = list(input())
S3 *= 5
# print(S1)
# print(S2)
# print(S3)

ans = 1000000000
for i1 in range(len(S1)):
    for i2 in range(len(S2)):
        if i1 == i2:
            continue
        for i3 in range(len(S3)):
            if i1 == i3 or i2 == i3:
                continue

            if S1[i1] == S2[i2] == S3[i3]:
                # print(i1, i2, i3)
                ans = min(ans, max([i1, i2, i3]))

if ans == 1000000000:
    print(-1)
else:
    print(ans)
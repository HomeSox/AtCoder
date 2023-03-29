import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

is_call = [False for _ in range(N + 1)]

for i, a in enumerate(A):

    # print(i+1, a, is_call)
    if is_call[i+1]:
        continue

    is_call[a] = True


ans = []
for i, ic in enumerate(is_call[1:]):

    if ic:
        continue

    ans.append(i+1)


ans.sort()

print(len(ans))
print(*ans)



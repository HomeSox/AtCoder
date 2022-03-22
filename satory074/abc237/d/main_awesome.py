from collections import deque

N = int(input())
S = input()

A = deque([N])
for i in range(N, 0, -1):
    if S[i-1] == 'L':
        A.append(i - 1)
    else:
        A.appendleft(i - 1)

print(*A)
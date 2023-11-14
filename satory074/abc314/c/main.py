from collections import deque
import sys

N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

colors = [deque() for _ in range(M + 1)]
for i in range(N):
    colors[C[i]].append(S[i])

for i in range(1, M + 1):
    if not colors[i]:
        continue

    colors[i].appendleft(colors[i].pop())

# print(colors)

ans = ""
for i in range(N):
    ans += colors[C[i]].popleft()

print(ans)

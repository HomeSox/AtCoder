from collections import deque

N, X = map(int, input().split())
S = input()

ans = deque(bin(X))
for s in S:
    if s == 'U':
        deque.pop(ans)
        continue

    if s == 'L':
        deque.append(ans, '0')
        continue

    if s == 'R':
        deque.append(ans, '1')
        continue


print(int(''.join(ans), 2))

from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())

    G[A].append(B)
    G[B].append(A)


st = 1
distance = [-1] * (N + 1)
distance[st] = 0
queue = deque([st])
ans = [-1 for _ in range(N + 1)]

while queue:
    current_node = queue.popleft()
    for neighbor in G[current_node]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current_node] + 1
            ans[neighbor] = current_node
            queue.append(neighbor)

print("Yes")
for a in ans[2:]:
    print(a)

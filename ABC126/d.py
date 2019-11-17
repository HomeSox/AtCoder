N = int(input())
keirolist = [tuple(map(int, input().split())) for i in range(N-1)]

graph = [[] for _ in range(N+1)]
for (u, v, w) in keirolist:
  graph[u].append([v, w])
  graph[v].append([u, w])

root = 1
dist = [-1 for _ in range(N+1)]
dist[root] = 0

stack = [root]
while stack:
  idx = stack.pop()
  for i, w in graph[idx]:
    if dist[i] == -1:
      dist[i] = dist[idx] + w
      stack.append(i)

[print(0 if d % 2 == 0 else 1) for d in dist[1:]]
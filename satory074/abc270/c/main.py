N, X, Y = map(int, input().split())
X -= 1
Y -= 1

G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    G[u].append(v)
    G[v].append(u)

stack = [(X, -1)]
parent = [-1] * N
while stack:
    cur, p = stack.pop()
    for v in G[cur]:
        if v == p:
            continue

        parent[v] = cur
        stack.append((v, cur))

ans = []
cur = Y
while cur != X:
    ans.append(cur + 1)
    cur = parent[cur]

ans.append(X + 1)
print(*reversed(ans))

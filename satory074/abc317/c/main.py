N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1

    G[A].append((B, C))
    G[B].append((A, C))

def dfs(u, is_visited, length):
    is_visited[u] = True

    max_ = length
    for v, c in G[u]:
        if is_visited[v]:
            continue

        max_ = max(max_, dfs(v, is_visited, length + c))

    is_visited[u] = False

    return max_

ans = 0
for i in range(N):
    is_visited = [False] * N

    ans = max(ans, dfs(i, is_visited, 0))

print(ans)
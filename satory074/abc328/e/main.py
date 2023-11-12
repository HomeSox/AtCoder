import itertools
from collections import defaultdict, deque

N, M, K = map(int, input().split())
G = []
for _ in range(M):
    u, v, w = map(int, input().split())
    G.append((u, v, w))

ans = K
for cmb in itertools.combinations(G, N - 1):
    sum_ = sum(w for _, _, w in cmb)

    if sum_ % K >= ans:
        continue

    G_= defaultdict(set)
    for u, v, w in cmb:
        G_[u].add(v)
        G_[v].add(u)

    # bfs
    u0, v0, w0 = cmb[0]

    c = 1
    is_visited = [False for _ in range(N + 1)]
    is_visited[u0] = True

    pos = deque()
    pos.append(u0)

    while pos:
        cur = pos.popleft()
        for u in G_[cur]:
            if is_visited[u]:
                continue

            is_visited[u] = True
            pos.append(u)

            c += 1

    if c == N:
        ans = sum_ % K

print(ans)

N, M = map(int, input().split())

G = {}
ans = 0
for _ in range(M):
    u, v = map(int, input().split())

    if u > v:
        u, v = v, u

    if u == v:
        ans += 1
        # print(u, v)
        continue

    if u in G:
        if v in G[u]:
            ans += 1
            # print(u, v)
        else:
            G[u].append(v)
    else:
        G[u] = [v]

    # print(G)

print(ans)

import sys
sys.setrecursionlimit(10**6)

N = int(input())

G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for g in G:
    g.sort()

ans = []
def dfs(crr, pre):
    ans.append(crr)

    for nxt in G[crr]:
        if nxt != pre:
            dfs(nxt, crr)
            ans.append(crr)

dfs(1, -1)

print(*ans)

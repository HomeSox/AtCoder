import collections as cl
import math

import networkx as nx

N, M = map(int, input().split())

is_only = [True] * (N + 1)

edge_list = []
for _ in range(M):
    u, v = map(int, input().split())
    edge_list.append((u, v))

    is_only[u] = False
    is_only[v] = False


G = nx.Graph()
G.add_edges_from(edge_list)

ans = 0

for i in range(1, N + 1):
    if is_only[i]:
        ans += 1

ans += len(list(nx.connected_components(G)))

print(ans)

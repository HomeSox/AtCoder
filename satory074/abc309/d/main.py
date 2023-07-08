import heapq

N1, N2, M = map(int, input().split())

G1 = []
G2 = []
for _ in range(M):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    if 1 <= a <= N1 and 1 <= b <= N1:
        G1.append((a, b))
        continue

    if N1 + 1 <= a <= N1 + N2 and N1 + 1 <= b <= N1 + N2:
        G2.append((a, b))
        continue

G1.sort()
G2.sort()


# グラフを隣接リストとして表現
graph1 = [[] for _ in range(N1 + 1)]
graph2 = [[] for _ in range(N2 + 1)]

for a, b in G1:
    graph1[a].append(b)
    graph1[b].append(a)

for a, b in G2:
    a -= N1
    b -= N1
    graph2[a].append(b)
    graph2[b].append(a)


def dijkstra(graph, start):
    distance = [float("inf")] * len(graph)

    distance[start] = 0
    heap = [(0, start)]
    while heap:
        v_dist, v = heapq.heappop(heap)

        if distance[v] < v_dist:
            continue

        for nv in graph[v]:
            if distance[v] + 1 < distance[nv]:
                distance[nv] = distance[v] + 1
                heapq.heappush(heap, (distance[nv], nv))

    return distance


d1 = dijkstra(graph1, 1)
d2 = dijkstra(graph2, N2)

print(max(filter(lambda x: x != float("inf"), d1)) + max(filter(lambda x: x != float("inf"), d2)) + 1)

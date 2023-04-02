import heapq

Q = int(input())

heap = []
plus = 0
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        heapq.heappush(heap, query[1] - plus)
        continue

    if query[0] == 2:
        plus += query[1]
        continue

    if query[0] == 3:
        print(heapq.heappop(heap) + plus)
        continue

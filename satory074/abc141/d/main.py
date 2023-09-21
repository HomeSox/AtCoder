import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [-a for a in A]

pq = []
for a in A:
    heapq.heappush(pq, a)

for _ in range(M):
    min_ = heapq.heappop(pq)
    heapq.heappush(pq, -(-min_ // 2))

print(-sum(pq))

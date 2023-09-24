import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

l = sorted(P[:K])
heapq.heapify(l)

print(l[0])
for i, p in enumerate(P[K:]):
    heapq.heappush(l, p)

    heapq.heappop(l)

    print(l[0])

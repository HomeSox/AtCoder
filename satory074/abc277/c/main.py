from collections import defaultdict, deque

N = int(input())

G = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())

    G[A].append(B)
    G[B].append(A)

que = deque()
que.append(1)
is_visit = {1}
while que:
    v = que.popleft()

    for v_ in G[v]:
        if v_ in is_visit:
            continue

        que.append(v_)
        is_visit.add(v_)

print(max(is_visit))

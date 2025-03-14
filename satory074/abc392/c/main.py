N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

idxQ = [0] * (N + 1)
for i in range(N):
    idxQ[Q[i]] = i

ans = []
for i in range(1, N + 1):
    ans.append(Q[P[idxQ[i]] - 1])

print(*ans)

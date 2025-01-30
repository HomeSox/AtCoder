N, Q = map(int, input().split())

A = [0 for _ in range(N + 1)]

for _ in range(Q):
    L, R, T = map(int, input().split())

    for i in range(L, R + 1):
        A[i] = T

for a in A[1:]:
    print(a)

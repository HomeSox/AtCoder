import bisect

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

S = [a - i for i, a in enumerate(A)]

for _ in range(Q):
    k = int(input())
    print(bisect.bisect_right(S, k) + k)


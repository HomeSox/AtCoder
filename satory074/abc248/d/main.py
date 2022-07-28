import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

indexes = [[] for _ in range(N + 1)]

for i, a in enumerate(A):
    indexes[a].append(i + 1)

for _ in range(Q):
    L, R, X = map(int, input().split())

    st = bisect.bisect_left(indexes[X], L)
    gl = bisect.bisect_right(indexes[X], R)

    print(gl - st)

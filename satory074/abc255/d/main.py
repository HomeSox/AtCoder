import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

sortedA = sorted(A)

# 累積和
cumA = [0] * (N + 1)
for i in range(len(sortedA)):
    cumA[i + 1] = cumA[i] + sortedA[i]

# print(sortedA)
# print(cumA)

for _ in range(Q):
    X = int(input())
    idx = bisect.bisect_left(sortedA, X)

    absleft = abs(X * idx - cumA[idx])
    absright = abs(X * (N - idx) - (cumA[-1] - cumA[idx]))

    # print(X, idx, absleft, absright)
    print(absleft + absright)

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# print(A)
len_ = N - K
ans = float("inf")
for i in range(K + 1):
    # print(A[i : len_ + i])
    # A_ = A[i : len_ + i]
    ans = min(A[len_ + i - 1] - A[i], ans)

print(ans)

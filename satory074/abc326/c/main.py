N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

max_ = 0
idx = 0
for i in range(len(A)):
    while A[i] - A[idx] >= M:
        idx += 1

    max_ = max(max_, i - idx + 1)

print(max_)


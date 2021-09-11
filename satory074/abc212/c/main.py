N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

idx_a = 0
idx_b = 0
answer = 10 ** 9
while idx_a != N and idx_b != M:
    if (min_ := abs(A[idx_a] - B[idx_b])) < answer:
        answer = min_

    if A[idx_a] > B[idx_b]:
        idx_b += 1
    else:
        idx_a += 1

print(answer)

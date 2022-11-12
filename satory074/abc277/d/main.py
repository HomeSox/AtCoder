N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

maxes = [A[0]]
for a1, a2 in zip(A[:-1], A[1:]):
    if a1 == a2 or (a1 + 1) % M == a2:
        maxes[-1] += a2
    else:
        maxes.append(a2)

if A[0] == 0 and A[-1] == M - 1 and len(maxes) != 1:
    maxes[0] += maxes[-1]

print(sum(A) - max(maxes))

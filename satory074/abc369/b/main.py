N = int(input())

R = []
L = []
for _ in range(N):
    A, S = input().split()

    if S == "R":
        R.append(int(A))
        continue

    if S == "L":
        L.append(int(A))
        continue

r = 0
for r1, r2 in zip(R[:-1], R[1:]):
    r += abs(r2 - r1)

l = 0
for l1, l2 in zip(L[:-1], L[1:]):
    l += abs(l2 - l1)


print(l + r)

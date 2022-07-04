S = input()
K = int(input())

Q = [0] * (len(S) + 1)
for i, s in enumerate(S):
    Q[i + 1] = Q[i] + int(s == ".")

ans = 0
l = 0
for r in range(1, len(S) + 1):
    while Q[r] - Q[l] > K:
        l += 1

    ans = max(ans, r - l)

print(ans)

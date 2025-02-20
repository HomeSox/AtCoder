N, K = map(int, input().split())
S = input()

cur = 0
ans = 0
for s in S:
    if s == "O":
        cur += 1
    else:
        if cur >= 0:
            ans += cur // K
        cur = 0

if S[-1] == "O":
    ans += cur // K

print(ans)


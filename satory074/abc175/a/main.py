S = input()

cur = S[0]
curn = 1
ans = -1
for s in S[1:]:
    if s == cur:
        curn += 1
    else:
        if cur == 'R':
            ans = max(ans, curn)

        cur = s
        curn = 1

if cur == 'R':
    ans = max(ans, curn)

ans = max(ans, 0)

print(ans)

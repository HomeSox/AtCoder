S = input()

ma = 0
ans = 0
for s in S:
    if s == "R":
        ma += 1
    else:
        ans = max(ans, ma)
        ma = 0

print(ans)

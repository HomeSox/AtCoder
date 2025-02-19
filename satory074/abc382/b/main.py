N, D = map(int, input().split())
S = input()

ans = ''
for s in S[::-1]:
    if D <= 0:
        ans += s
    else:
        if s == "@":
            D -= 1
            ans += "."
        else:
            ans += s
print(ans[::-1])


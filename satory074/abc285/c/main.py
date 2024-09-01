S = input()

ans = 0
for i, s in enumerate(S[::-1]):
    ans += (ord(s) - ord("A") + 1) * 26**i

print(ans)

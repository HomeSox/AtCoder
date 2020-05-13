w = input()

ans = ''
for s in w:
  if not s in ['a', 'i', 'u', 'e', 'o']:
    ans += s

print(ans)

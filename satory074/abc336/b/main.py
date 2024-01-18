N = int(input())

ans = 0
for b in bin(N)[::-1]:
  if b == '0':
    ans += 1
  else:
    break

print(ans)

S = input()

ans = 0
left_white = 0
for i, s in enumerate(S):
  if s == 'W':
    ans += i - left_white
    left_white += 1

print(ans)

N = int(input())

is_one = True
ans = ''
for _ in range((N + 1) * 2):
  if is_one:
    ans += '1'
  else:
    ans += '0'

  is_one = not is_one

print(ans[:-1])

N, K= map(int, input().split())
S = input()

ans = ''
n_kessho = 0
for s in S:
  if n_kessho >= K:
    ans += 'x'
    continue
  
  if s == 'o':
    ans += 'o'
    n_kessho += 1
  else:
    ans += 'x'
  
print(ans)

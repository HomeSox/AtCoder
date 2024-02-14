Q = int(input())

ans = []
for _ in range(Q):
  n, x = map(int, input().split())
  
  if n == 1:
    ans.append(x)
    continue
  
  if n == 2:
    print(ans[-x])
    continue

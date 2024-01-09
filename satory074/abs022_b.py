N = int(input())

l = [False for _ in range(10 ** 5 + 1)]
ans = 0
for _ in range(N):
  A = int(input())
  
  if l[A]:
    ans += 1
  else:
    l[A] = True
  
print(ans)

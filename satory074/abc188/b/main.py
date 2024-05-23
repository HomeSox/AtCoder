N = input()
A = map(int, input().split())
B = map(int, input().split())

ans = 0
for a, b in zip(A, B):
  ans += a * b
  
if ans == 0:
  print('Yes')
else:
  print('No')
  

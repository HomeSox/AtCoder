N = int(input())
cnt = 0

for _ in range(N):
  D1, D2 = map(int, input().split())
  
  if D1 == D2:
    cnt += 1
    
    if cnt == 3:
      print('Yes')
      exit()
  
  else:
    cnt = 0

print('No')

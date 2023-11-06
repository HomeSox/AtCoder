N, T = input().split()

ans = []
for i in range(int(N)):
  S = input()
  
  if S == T:
    ans.append(i + 1)
    continue
    
  if abs(len(S) - len(T)) > 1:
    continue
  
  if len(S) < len(T):
    s1, s2 = S, T
  else:
    s1, s2 = T, S
  
  i1, i2 = 0, 0
  miss = 0
  while miss <= 1 and i1 < len(s1) and i2 < len(s2):
    if s1[i1] != s2[i2]:
      miss += 1
      
      i2 += 1
      
      if len(s1) == len(s2):
        i1 += 1
      
      continue
    
    i1 += 1
    i2 += 1
  
  # print(T, S, miss)
  if miss <= 1:
    ans.append(i + 1)

print(len(ans))
print(*ans)
  

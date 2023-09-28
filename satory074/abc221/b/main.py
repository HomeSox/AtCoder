S = input()
T = input()

ans = 0
for i in range(len(S) - 1):
  if S[i] != T[i]:
    if S[i] == T[i + 1] and S[i + 1] == T[i]:
      print('Yes')
    else:
      print('No')
      
    exit()

print('Yes')

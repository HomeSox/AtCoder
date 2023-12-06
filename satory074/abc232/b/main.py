S = input()
T = input()

K = (ord(S[0]) - ord(T[0]) + 26) % 26

for s, t in zip(S, T):
  if (ord(s) - ord(t) + 26) % 26 == K:
    continue
  
  print('No')
  exit()

print('Yes')

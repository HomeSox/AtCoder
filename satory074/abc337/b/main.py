S = input()
l = ['A', 'B', 'C']

idx = 0
for l_ in l:
  while idx < len(S) and S[idx] == l_:
    idx += 1

if len(S) == idx:
  print('Yes')
else:
  print('No')

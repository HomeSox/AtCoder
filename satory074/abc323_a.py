S = input()
for i, s in enumerate(S):
  if i % 2 == 1:
    if s == '1':
      print('No')
      break
else:
  print('Yes')

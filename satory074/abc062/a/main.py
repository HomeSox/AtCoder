l = [[1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2]]
x, y = map(int, input().split())

for l_ in l:
  if x in l_:
    if y in l_:
      print('Yes')
    else:
      print('No')
    
    break

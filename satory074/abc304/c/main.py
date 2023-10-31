N, D = map(int, input().split())

XY = []
for _ in range(N):
  X, Y = map(int, input().split())
  XY.append([X, Y])
  
# print(XY)

is_kansen = [False for _ in range(N)]
is_kansen[0] = True

baramaku = [XY[0]]
while baramaku:
  x, y = baramaku.pop()
  
  # print(x, y)
  for i, (x_, y_) in enumerate(XY):
    if is_kansen[i]:
      continue
    
    if (((x - x_) ** 2) + (y - y_) ** 2) ** 0.5 <= D:
      is_kansen[i] = True
      baramaku.append(XY[i])
  
for b in is_kansen:
  if b:
    print('Yes')
  else:
    print('No')

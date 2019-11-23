X, Y = map(int, input().split())

shokin = [300000, 200000, 100000]

total = 0
if X <= 3:
  total += shokin[X-1]
if Y <= 3:
  total += shokin[Y-1]
if X == 1 and Y == 1:
  total += 400000

print(total)

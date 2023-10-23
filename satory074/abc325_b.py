N = int(input())
WX = [list(map(int, input().split())) for _ in range(N)]

ans = -1
for t in range(0, 24):
  sankasha = 0
  for i2, (w2, x2) in enumerate(WX):
    # print((x2 + t) % 24)
    if 9 <= (x2 + t) % 24 <= 17:
      sankasha += w2
  
  ans = max(ans, sankasha)
  # print()

print(ans)

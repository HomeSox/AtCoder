K, G, M = map(int, input().split())

g = 0
m = 0
for _ in range(K):
  if g == G:
    g = 0
  elif m == 0:
    m = M
  else:
    w = min(G - g, m)
    m -= w
    g += w

print(g, m)
  

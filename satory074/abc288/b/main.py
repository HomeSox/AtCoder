N, K = map(int, input().split())

l = [input() for _ in range(K)]

l.sort()

for l_ in l:
  print(l_)

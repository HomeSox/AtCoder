N = int(input())

l = list(range(1, 2*N+2))

while l:
  print(l.pop(0))

  inp = int(input())
  if inp == 0:
    exit()
  else:
    l.pop(l.index(inp))

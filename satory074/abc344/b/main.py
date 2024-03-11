A = []
while True:
  try:
    n = int(input())
    A.append(n)
  except:
    break

for a in A[::-1]:
  print(a)

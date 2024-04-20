l = []

for _ in range(5):
  l.append(int(input()))

k = int(input())

for i in range(5):
  for j in range(5):
    if i == j:
      continue
    
    if abs(l[i] - l[j]) > k:
      print(':(')
      exit()

print('Yay!')

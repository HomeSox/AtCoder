S = input()

a = -1
z = -1
for i, s in enumerate(S):
  if a < 0 and s == 'A':
    a = i
  
  if s == 'Z':
    z = i

print(z - a + 1)

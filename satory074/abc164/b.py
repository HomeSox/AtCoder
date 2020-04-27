A, B, C, D = map(int, input().split())

is_tkhs = True
for _ in range(100000):
  if is_tkhs:
    C -= B
  else:
    A -= D

  is_tkhs = not (is_tkhs)

  if C <= 0 or A <= 0:
    break

print('No' if A <= 0 else 'Yes')
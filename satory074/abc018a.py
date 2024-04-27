A = int(input())
B = int(input())
C = int(input())

if A > B > C:
  print(1)
  print(2)
  print(3)

if A > C > B:
  print(1)
  print(3)
  print(2)

if B > A > C:
  print(2)
  print(1)
  print(3)

if B > C > A:
  print(3)
  print(1)
  print(2)

if C > A > B:
  print(2)
  print(3)
  print(1)
  
if C > B > A:
  print(3)
  print(2)
  print(1)

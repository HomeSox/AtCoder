# = map(int, input())
N = int(input())

ans = []
while N != 0 and N != 1:
  if N % 2 == 0:
    N = N // 2
    ans.append('B')
  else:
    N -= 1
    ans.append('A')

if N == 0:
  ans.append('B')
  ans.append('A')
else:
  ans.append('A')

print(''.join(ans[::-1]))

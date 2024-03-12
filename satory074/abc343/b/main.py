N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
# print(A)

for row in A:
  ans = []
  for i, n in enumerate(row):
    if n == 1:
      ans.append(i + 1)
    
  print(*ans)

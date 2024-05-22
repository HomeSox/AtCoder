N = int(input())
S = list(map(int, input().split()))

# print(S)

ans = [S[0]]

for s in S[1:]:
  ans.append(s - sum(ans))
  
print(*ans)

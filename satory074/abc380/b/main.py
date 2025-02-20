S = input().split("|")
# print(S)

ans = [len(s) for s in S[1:-1]]
print(*ans)

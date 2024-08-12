N = int(input())
S = [input() for _ in range(N)]

ma = max(len(s) for s in S)
ans = []
for i in range(ma):
    column = []
    for s in reversed(S):
        if i < len(s):
            column.append(s[i])
        else:
            column.append("*")

    ans.append("".join(column).rstrip("*"))

for a in ans:
    print(a)

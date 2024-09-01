S = list(input())

d = []
for i in range(len(S)):
    S = [S.pop()] + S
    d.append("".join(S))

d.sort()

# print(d)
print(d[0])
print(d[-1])

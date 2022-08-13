import collections as cl
import math

H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]

H2, W2 = map(int, input().split())
B = [list(input().split()) for _ in range(H2)]


indexes = []
for h in range(H):
    l = []
    for w in range(W):
        for h2 in range(H2):
            for w2 in range(W2):
                if A[h][w] == B[h2][w2]:
                    l.append((h, w))
    indexes.append(list(set(l)))

print(indexes)
exit()


ans = []
for idx in indexes2:
    for i, b in enumerate(B):
        # print(idx, b)
        if idx == b:
            ans.append(i)

print(ans)


if len(set(ans)) != 2:
    print("No")
    exit()

print(list(set(ans)), list(range(H2)))
if list(set((ans))) == list(range(H2)):
    print("Yes")
else:
    print("No")

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

# 行と列を入れ替える
S = list(map(list, zip(*S)))
T = list(map(list, zip(*T)))

S = [''.join(l) for l in S]
T = [''.join(l) for l in T]

S.sort()
T.sort()

# print(S)
# print(T)

if S == T:
    print('Yes')
else:
    print('No')

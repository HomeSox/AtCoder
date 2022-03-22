import collections as cl

N = int(input())
S = input()

idx = {}
for i in range(N + 1):
    idx[i] = -1

idx[0] = 0

for i, s in enumerate(S):
    if s == 'L':
        idx[i+1] = idx[i]
        idx[i] += N - i
    else: # R
        idx[i+1] = idx[i] + 1

ans = list(range(N + 1))
for k, v in idx.items():
    ans[v] = k

print(*(ans))
# print(' '.join(map(str, ans)))

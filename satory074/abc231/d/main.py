import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

par = [-1 for _ in range(10 ** 5 +1)]
def root(x):
    if par[x] < 0:
        return x

    par[x] = root(par[x])

    return par[x]

def unite(x, y):
    x = root(x)
    y = root(y)

    if x == y:
        return

    par[x] += par[y]
    par[y] = x

degree = [0] * (10 ** 5 + 1)
for _ in range(M):
    a, b = map(int, input().split())

    degree[a] += 1
    degree[b] += 1

    if root(a) == root(b):
        print('No')
        exit()

    unite(a, b)

if max(degree) <= 2:
    print('Yes')
else:
    print('No')

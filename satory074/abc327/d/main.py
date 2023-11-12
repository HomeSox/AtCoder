import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def dfs(g, node, num_01, c):
    num_01[node] = c
    for tonari in g[node]:
        if tonari in num_01:
            if num_01[tonari] == num_01[node]:
                return False
        else:
            if not dfs(g, tonari, num_01, 1 - c):
                return False

    return True


G = defaultdict(list)
num_01 = {}
for i in range(M):
    if A[i] == B[i]:
        print("No")
        exit()

    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

for node in range(1, N + 1):
    if node not in num_01:
        if not dfs(G, node, num_01, 0):
            print("No")
            exit()

print("Yes")

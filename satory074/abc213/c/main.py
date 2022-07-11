H, W, N = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())

    A.append(a)
    B.append(b)

dict_A = {}
for i, a in enumerate(sorted(list(set(A)))):
    dict_A[a] = i + 1

dict_B = {}
for i, b in enumerate(sorted(list(set(B)))):
    dict_B[b] = i + 1

for a, b in zip(A, B):
    print(dict_A[a], dict_B[b])
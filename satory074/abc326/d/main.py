N = int(input())
R = list(input())
C = list(input())

is_A = [[True for _ in range(N)] for _ in range(N)]
is_B = [[True for _ in range(N)] for _ in range(N)]
is_C = [[True for _ in range(N)] for _ in range(N)]

def kakutei(s, i, j):
    if s == 'A':
        for k in range(N):
            if k == i:
                continue

            is_A[i][k] = False

        for k in range(N):
            if k == j:
                continue

            is_A[k][j] = False

        is_B[i][j] = False
        is_C[i][j] = False

        return

    if s == 'B':
        for k in range(N):
            if k == i:
                continue

            is_B[i][k] = False

        for k in range(N):
            if k == j:
                continue

            is_B[k][j] = False

        is_A[i][j] = False
        is_C[i][j] = False

        return

    if s == 'C':
        for k in range(N):
            if k == i:
                continue

            is_C[i][k] = False

        for k in range(N):
            if k == j:
                continue

            is_C[k][j] = False

        is_A[i][j] = False
        is_B[i][j] = False

        return

if R[0] != C[0]:
    print('No')
    exit()
else:
    kakutei(R[0], 0, 0)

[print(l) for l in is_A]
print()
[print(l) for l in is_B]
print()
[print(l) for l in is_C]



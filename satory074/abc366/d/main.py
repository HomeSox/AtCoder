N = int(input())
A = []
for _ in range(N):
    l = []
    for _ in range(N):
        l.append(list(map(int, input().split())))
    A.append(l)

S = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            S[i + 1][j + 1][k + 1] = (
                S[i][j + 1][k + 1]
                + S[i + 1][j][k + 1]
                + S[i + 1][j + 1][k]
                - S[i][j][k + 1]
                - S[i][j + 1][k]
                - S[i + 1][j][k]
                + S[i][j][k]
                + A[i][j][k]
            )

Q = int(input())
for _ in range(Q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    result = (
        S[rx][ry][rz]
        - S[lx - 1][ry][rz]
        - S[rx][ly - 1][rz]
        - S[rx][ry][lz - 1]
        + S[lx - 1][ly - 1][rz]
        + S[lx - 1][ry][lz - 1]
        + S[rx][ly - 1][lz - 1]
        - S[lx - 1][ly - 1][lz - 1]
    )
    print(result)

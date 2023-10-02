N, M = map(int, input().split())
PCF = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        Pi, Ci, *Fi = PCF[i]
        Pj, Cj, *Fj = PCF[j]

        li = set(Fi)
        lj = set(Fj)

        if Pj <= Pi and li.issubset(lj):
            if Pj < Pi or lj - li:
                print('Yes')
                exit()

print('No')

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

# Tの組み合わせを全列挙
from itertools import product

l = []
for i in product(range(K), repeat=N):
    l.append(i)

for l_ in l:
    xor = 0
    for j in range(N):
        xor ^= T[j][l_[j]]

    if xor == 0:
        print("Found")
        exit()

print("Nothing")

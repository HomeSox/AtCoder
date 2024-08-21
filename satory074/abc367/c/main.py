from itertools import product

N, K = map(int, input().split())
R = list(map(int, input().split()))

sequences = list(product(range(1, 6), repeat=N))

ans = []
for l in sequences:
    if sum(l) % K != 0:
        continue

    for l_, r in zip(l, R):
        if l_ > r:
            break
    else:
        ans.append(l)

ans.sort()

for a in ans:
    print(*a)

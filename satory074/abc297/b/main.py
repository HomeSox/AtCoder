S = input()

k = []
q = []
r = []
b = []
n = []
for i, s in enumerate(S):
    if s == 'K':
        k.append(i)
        continue

    if s == 'Q':
        q.append(i)
        continue

    if s == 'R':
        r.append(i)
        continue

    if s == 'B':
        b.append(i)
        continue

    if s == 'N':
        n.append(i)
        continue


if b[0] % 2 == b[1] % 2:
    print('No')
    exit()

if r[0] < k[0] < r[1]:
    print('Yes')
else:
    print('No')

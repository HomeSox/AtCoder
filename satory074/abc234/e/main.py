X = int(input())
sX = str(X)

if len(sX) == 1:
    print(X)
    exit()

l = []
for i1 in range(0, 2):
    for diff_ in range(-9, 10):
        if int(sX[0]) + i1 >= 10:
            continue

        sn = str(int(sX[0]) + i1)
        for i2 in range(1, len(sX)):
            n = int(sn[-1]) + diff_
            if 0 <= n <= 9:
                sn += str(n)
            else:
                break
        else:
            if int(sn) >= X:
                l.append(int(sn))

# print(sorted(l))
print(min(l))


K = int(input())

l = []
for i1 in range(0, 10):
    l.append(i1)
    for i2 in range(0, 10):
        if i1 <= i2:
            continue

        l.append(i1 * 10 + i2)

        for i3 in range(0, 10):
            if i2 <= i3:
                continue

            l.append(i1 * 100 + i2 * 10 + i3)

            for i4 in range(0, 10):
                if i3 <= i4:
                    continue

                l.append(i1 * 1000 + i2 * 100 + i3 * 10 + i4)

                for i5 in range(0, 10):
                    if i4 <= i5:
                        continue

                    l.append(i1 * 10000 + i2 * 1000 + i3 * 100 + i4 * 10 + i5)

                    for i6 in range(0, 10):
                        if i5 <= i6:
                            continue

                        l.append(i1 * 100000 + i2 * 10000 + i3 * 1000 + i4 * 100 + i5 * 10 + i6)

                        for i7 in range(0, 10):
                            if i6 <= i7:
                                continue

                            l.append(i1 * 1000000 + i2 * 100000 + i3 * 10000 + i4 * 1000 + i5 * 100 + i6 * 10 + i7)

                            for i8 in range(0, 10):
                                if i7 <= i8:
                                    continue

                                l.append(i1 * 10000000 + i2 * 1000000 + i3 * 100000 + i4 * 10000 + i5 * 1000 + i6 * 100 + i7 * 10 + i8)

                                for i9 in range(0, 10):
                                    if i8 <= i9:
                                        continue

                                    l.append(i1 * 100000000 + i2 * 10000000 + i3 * 1000000 + i4 * 100000 + i5 * 10000 + i6 * 1000 + i7 * 100 + i8 * 10 + i9)

                                    for i10 in range(0, 10):
                                        if i9 <= i10:
                                            continue

                                        l.append(i1 * 1000000000 + i2 * 100000000 + i3 * 10000000 + i4 * 1000000 + i5 * 100000 + i6 * 10000 + i7 * 1000 + i8 * 100 + i9 * 10 + i10)

l.sort()

print(l[K])


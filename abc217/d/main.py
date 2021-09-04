import bisect

L, Q = map(int, input().split())

cutx = [0, L]
for _ in range(Q):
    c, x = map(int, input().split())

    # print(idx, cutx)
    if c == 1:
        bisect.insort_left(cutx, x)
    elif c == 2:
        if not cutx:
            print(L)
            continue
        idx = bisect.bisect(cutx, x)
        print(cutx[idx] - cutx[idx-1])
import array
import bisect

L, Q = map(int, input().split())

cutx = array.array('i', [0, L])
for _ in range(Q):
    c, x = map(int, input().split())

    if c == 1:
        bisect.insort(cutx, x)
    else:
        idx = bisect.bisect(cutx, x)
        print(cutx[idx] - cutx[idx-1])
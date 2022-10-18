import collections as cl
import math

H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]

H2, W2 = map(int, input().split())
B = [list(input().split()) for _ in range(H2)]

# bit全探索
for ih in range(2**H):
    bh = bin(ih)[2:].zfill(H)
    for iw in range(2**W):
        bw = bin(iw)[2:].zfill(W)

        A2 = []
        # print(bh, bw)
        for h, bh_ in enumerate(bh):
            l = []
            if bh_ == '0':
                continue

            for w, bw_ in enumerate(bw):
                if bw_ == '0':
                    continue

                l.append(A[h][w])

            if l:
                A2.append(l)


        if A2 == B:
            print('Yes')
            exit()

print('No')


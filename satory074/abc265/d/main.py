import bisect
import collections as cl
import math

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

PQR = P + Q + R

cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + A[i]
# print(cum)

l = 0
r = 1
while True:
    if r >= (N + 1):
        break

    sum_ = cum[r] - cum[l]
    # print(l, r, sum_)

    if sum_ == PQR:
        li = A[l:r]
        if len(li) < 3:
            break

        cum_li = cum[l : r + 1]

        ll = bisect.bisect_left(cum_li, P + cum[l])
        rr = bisect.bisect_left(cum_li, P + Q + cum[l])
        P_ = cum_li[ll] - cum_li[0]
        Q_ = cum_li[rr] - cum_li[ll]
        R_ = cum_li[-1] - cum_li[rr]

        # print(li)
        # print(cum_li)
        # print(ll, rr)
        # print(P_, Q_, R_)

        if P == P_ and Q == Q_ and R == R_:
            print("Yes")
            exit()
        else:
            r += 1
            l += 1
    else:
        if sum_ < PQR:
            r += 1
        else:
            l += 1

print("No")

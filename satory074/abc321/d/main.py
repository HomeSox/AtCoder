import bisect

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# 累積和
QB = [0]
for b in B:
    QB.append(QB[-1] + b)


# print(B)
ans = 0
for i, a in enumerate(A):
    n = P - a

    idx = bisect.bisect_left(B, n)

    left = QB[idx] + a * idx
    right = P * (M - idx)
    ans += left + right
    # print(a, n)
    # print(left, right, ans)

print(ans)



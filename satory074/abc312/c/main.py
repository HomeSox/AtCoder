N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

l, r =  0, 10 ** 9 + 1
while r - l > 1:
    m = (l + r) // 2

    c_A = len([i for i in A if i <= m])
    c_B = len([i for i in B if i >= m])

    if c_A >= c_B:
        r = m
    else:
        l = m

print(r)

N, a, b = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 10 ** 9 + 1

while r - l > 1:
    m = (l + r) // 2

    n_plus, n_minus = 0, 0
    for i, a_ in enumerate(A):
        if a_ < m:
            n_plus += (m - a_ + a - 1) // a
        else:
            n_minus += (a_ - m) // b

    if n_plus <= n_minus:
        l = m
    else:
        r = m

print(l)

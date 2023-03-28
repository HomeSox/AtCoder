T = int(input())

for _ in range(T):
    n = int(input())

    a = 0
    for i in range(2, n):
        if n % i == 0:
            a = i
            break

    if n % (a * a) == 0:
        p = a
        q = n // a // a
    else:
        p = int((n // a) ** 0.5)
        q = a

    print(p, q)

X = int(input())


def prime_number(x):
    if x < 2:
        return 2
    else:
        for i in range(2, x):
            if x % i == 0:
                return prime_number(x + 1)
        return x


print(prime_number(X))

t = int(input())


def f(n):
    return n ** 2 + n * 2 + 3


print(f(f(f(t) + t) + f(f(t))))


N = int(input())


def f(n):
    if n == 0:
        return ["#"]
    else:
        g = ["." * n for _ in range(n)]
        g_ = f(n - 1)

        G = g_ + g_ + g_
        G += g_ + g + g_
        G += g_ + g_ + g_

        return G


print(f(N))

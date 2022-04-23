import collections as cl
import math


def divisors(n):
    """約数列挙
    Args:
        n (int): 約数列挙する数字
    Returns:
        List[int]: [約数1, 約数2, ...]
    Examples:
        >>> divisors(40)
        [1, 2, 4, 5, 8, 10, 20, 40]
    """
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


N = int(input())
A = list(map(int, input().split()))
clcA = cl.Counter(A)
# print(clcA)

ans = 0
for a in A:
    for n in divisors(a):
        n1 = n
        n2 = a // n1

        ans += clcA[n1] * clcA[n2]
        # print(a, n1, n2, ans)

print(ans)

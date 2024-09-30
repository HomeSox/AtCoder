import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


N = int(input())

if N == 1:
    print("Not Prime")
    exit()

if is_prime(N):
    print("Prime")
else:
    tail = int(str(N)[-1])
    if (tail % 2 != 0 and tail != 5) and (N % 3 != 0):
        print("Prime")
    else:
        print("Not Prime")

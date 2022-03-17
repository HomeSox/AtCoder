import math
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

N, X = map(int, input().split())
x = list(map(int, input().split()))
x = [abs(x_ - X) for x_ in x]

print(my_gcd(*x))

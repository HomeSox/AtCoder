# 公式解説: https://atcoder.jp/contests/abc215/editorial/2482

import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

def factorization(n):
    """ 素因数分解
    Args:
        n (int): 素因数分解する数字
    Returns:
        List[List[int, int]]: [[素数, 累乗], ...]
    Examples:
        >>> factorization(40)
        [[2, 3], [5, 1]]
    """
    arr = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            c = 0
            while n % i == 0:
                c += 1
                n //= i
            arr.append([i, c])

    if n != 1:
        arr.append([n, 1])

    return arr

# > gcd(a,b) != 1 であるとは、 a と b とが何らかの共通の素因数を持っているということです。
# > このことから、エラトステネスの篩の要領の、以下の解法が成立します。

# > - 集合 S に 1 から M まで全ての整数を入れる。
S = list(range(1, M + 1))
prime = [] # 素数リスト

# > - i が 1 から N まで、以下を繰り返す。
for i in range(1, N + 1):
    # > - A_i を素因数分解する。素因数の集合を P とする。
    P = [n for n, _ in factorization(A[i-1])]

    # > - P に含まれる全ての素因数 k について、「Sからkの倍数をすべて削除する」という操作を行う。
    for k in P:
        # > - なお、全体を通して同じ素因数に関して2度以上操作を行う必要がないことを利用して、計算量を改善できる。(この部分を行わないとTLEします)
        if k not in prime:
            S = [s for s in S if s % k != 0]
            prime.append(k)

print(len(S))
[print(s) for s in S]
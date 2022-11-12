import collections as cl
import math

N = int(input())
a = list(map(int, input().split()))

# 約数
def divisor(n):
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    return ans


kouho = divisor(a[0])
for a_ in a:
    # print(a_, divisor(a_))

    divlist = divisor(a_)
    if 2 not in divlist:
        if 3 not in divlist:
            if a_ != 1:
                print(-1)
                exit()

    kouho = [k for k in kouho if k in divlist]

shusoku = max(kouho)

ans = 0
for a_ in a:
    n = a_
    # print(n)

    for _ in range(10**9):
        if n % 3 == 0:
            n //= 3
            ans += 1
        else:
            break
    # print(n)

    for _ in range(10**9):
        if n % 2 == 0:
            n //= 2
            ans += 1
        else:
            break

    # print(ans)
    # print()

print(ans)

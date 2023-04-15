import collections as cl
import math
from collections import deque

Q = int(input())
MOD = 998244353

ans = deque('1')
remainder = 1
for _ in range(Q):
    ipt = list(map(int, input().split()))

    if ipt[0] == 1:
        x = ipt[1]

        ans.append(str(x))
        remainder = (remainder * 10 + x) % MOD
        continue

    if ipt[0] == 2:
        # ansの最初の要素を削除
        r = int(ans.popleft())
        remainder = (remainder - r * pow(10, len(ans), MOD) + MOD) % MOD
        continue

    if ipt[0] == 3:
        print(remainder)
        continue


    # print(ipt, ans)


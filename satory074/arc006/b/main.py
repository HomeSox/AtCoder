import collections as cl
import math

N, L = map(int, input().split())

amida = [list(input()) for _ in range(L + 1)]
amida = amida[::-1]

ans = amida[0].index('o') + 1

for a in amida[1:]:
    if ans > 1 and a[ans - 2] == '-':
        ans -= 2
    elif ans < N * 2 - 1 and a[ans] == '-':
        ans += 2

print(ans // 2 + 1)
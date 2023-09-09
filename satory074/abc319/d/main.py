import collections as cl
import math

N, M = map(int, input().split())
L = list(map(int, input().split()))

# print(sum(L) + (N - 1))


def check(arr, k, mid):
    cnt = 1
    s = 0
    for a in arr:
        if s + a > mid:
            cnt += 1
            s = a + 1
        else:
            s += a + 1

    return cnt <= k


low = max(L)
high = sum(L)

ans = high
while low <= high:
    mid = (low + high) // 2
    if check(L, M, mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)


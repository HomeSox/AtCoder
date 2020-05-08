N, K, M = map(int, input().split())
A = list(map(int, input().split()))

mokuhyou = N*M

A_sum = sum(A)


ans = mokuhyou-A_sum

if ans < 0:
    print(0)
elif ans > K:
    print(-1)

else:print(ans)



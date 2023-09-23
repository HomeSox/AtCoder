import collections as cl
import math

T = int(input())
for _ in range(T):
    N, X, K = map(int, input().split())

    # K = 0 の場合、答えは1
    if K == 0:
        print(1)
        continue

    # K = 1 の場合、答えはXの子の数（最大で2）
    if K == 1:
        if 2*X <= N and 2*X + 1 <= N:
            print(2)
        elif 2*X <= N:
            print(1)
        else:
            print(0)
        continue

    # K > 1 の場合
    cnt = 0
    min_val = X * 2**(K)
    max_val = (X + 1) * 2**(K) - 1

    # 実際に存在する頂点だけをカウント
    for i in range(min_val, max_val + 1):
        if i <= N:
            cnt += 1

    print(cnt)

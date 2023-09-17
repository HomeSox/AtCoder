T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    tmp = N
    min_ = 0
    while tmp:
        min_ += tmp % 3
        tmp //= 3

    if abs(N - K) % 2 == 0:
        if min_ <= K and K <= N:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
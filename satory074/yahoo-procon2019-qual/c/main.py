K, A, B = list(map(int, input().split()))

if B - A <= 2:
    print(K + 1)
else:
    K -= A - 1
    print(int(K // 2 * (B - A) + K % 2 + A))

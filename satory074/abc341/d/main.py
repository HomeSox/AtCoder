N, M, K = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

lcm = N * M // gcd(N, M)
left, right = 1, 10 ** 18
while left < right:
    mid = (left + right) // 2
    count = mid // N + mid // M - (mid // lcm) * 2

    if count  < K:
        left = mid + 1
    else:
        right = mid

print(right)

def reverse_number(n):
    return int(str(n)[::-1])


N, K = map(int, input().split())


def f(x):
    min_x = x
    seen = set()
    while x not in seen:
        seen.add(x)
        min_x = min(min_x, x)
        x = reverse_number(x)
    return min_x


# Kから始めて、その逆数も含めて候補を生成
candidates = set()
x = K
while x <= N:
    if f(x) == K:
        candidates.add(x)
    x *= 10

x = reverse_number(K)
while x <= N:
    if f(x) == K and x not in candidates:
        candidates.add(x)
    x *= 10

print(len(candidates))

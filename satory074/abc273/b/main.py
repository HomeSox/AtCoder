from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal

N, K = map(int, input().split())

for i in range(K):
    N = Decimal(N).quantize(Decimal(f"1E{i+1}"), rounding=ROUND_HALF_UP)

print(int(N))

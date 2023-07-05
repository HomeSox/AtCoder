L1, R1, L2, R2 = map(int, input().split())

if min(R1, R2) - max(L1, L2) >= 0:
    print(min(R1, R2) - max(L1, L2))
else:
    print(0)

n = int(input())
MOD = 10007


prev1 = 0
prev2 = 0
prev3 = 0
for i in range(1, n - 1):
    # print(prev1)
    # print(prev2)
    # print(prev3)
    # print()

    if i == 1:
        prev1 = 1
        prev2 = 0
        prev3 = 0
        continue

    if i == 2:
        prev1 = 1
        prev2 = 1
        prev3 = 0
        continue

    # トリボナッチ数列の定義
    prev1, prev2, prev3 = (prev1 + prev2 + prev3) % MOD, prev1, prev2

print(prev1)
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

answer = [0 for _ in range(10)]

keisuu_table = [0 for _ in range(10)]
keisuu_table[A[0]] = 1
for a in A[1:]:
    num_kouho = []
    for n, k in enumerate(keisuu_table):
        if k == 0:
            continue
        # print(n, k)

        result_plus = (n + a) % 10
        result_mult = (n * a) % 10

        for _ in range(k):
            num_kouho.append(result_plus)
            num_kouho.append(result_mult)

    keisuu_table = [0 for _ in range(10)]
    for n in list(set(num_kouho)):
        keisuu_table[n] += num_kouho.count(n)

    # print(num_kouho)
[print(k) for k in keisuu_table]








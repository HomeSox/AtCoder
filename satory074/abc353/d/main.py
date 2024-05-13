from collections import defaultdict

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)

for num in A:
    length = len(str(num))
    d[length] += 1

res = 0
p10 = [10**i for i in range(11)]

for i, num in enumerate(A):
  res += num * i  # f(*, A[i]) の寄与
  length = len(str(num))
  d[length] -= 1

  # f(A[i], *) の寄与
  for length, count in d.items():
      res += num * p10[length] * count
      res %= MOD

print(res)

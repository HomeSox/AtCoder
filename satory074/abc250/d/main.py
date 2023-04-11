import bisect

N = int(input())
n = 10 ** 6 + 10

prime = {i for i in range(2, n)}

for i in range(2, n):
    if i in prime:
        for j in range(i * 2, n, i):
            if j in prime:
                prime.remove(j)

prime = list(prime)
prime.sort()

ans = 0
for p in prime[::-1]:
    div = N // pow(p, 3)
    ans += bisect.bisect(prime, min(div, p - 1))

print(ans)

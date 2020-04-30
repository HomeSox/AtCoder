k, n = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
q = [an - ap for an, ap in zip(a[1:], a[:-1])]

nomal = max(a) - min(a)
abnomal = k - max(q)

print(min(nomal, abnomal))

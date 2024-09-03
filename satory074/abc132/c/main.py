N = int(input())
d = list(map(int, input().split()))

d.sort()

m = int(N / 2)

print(d[m] - d[m - 1])

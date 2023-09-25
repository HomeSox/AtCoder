N, M = map(int, input().split())

d = N
l = []
for i in range(1, 10):
    mod = 0
    for j in range(1, N + 1):
        mod = (mod * 10 + i) % M
        if mod == 0:
            l.append((j, i))

if not l:
    print(-1)
else:
    l.sort(reverse=True)
    d, num = l[0]

    print(str(num) * d)

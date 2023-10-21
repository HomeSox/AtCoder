import bisect as bs

N = int(input())

slimes = {}
gouseiable = []
for _ in range(N):
    S, C = map(int, input().split())

    slimes[S] = C

    if C != 1:
        gouseiable.append(S)

gouseiable.sort()

while gouseiable:
    s = gouseiable.pop()

    if s * 2 in slimes:
        slimes[s * 2] += slimes[s] // 2
    else:
        slimes[s * 2] = slimes[s] // 2

    if slimes[s * 2] >= 2:
        bs.insort_left(gouseiable, s * 2)

    slimes[s] = slimes[s] % 2

# print(slimes)

print(sum(slimes.values()))

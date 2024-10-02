N = int(input())
intervals = []
idx = 1
for _ in range(N):
    L, R = map(int, input().split())
    intervals.append((L, R))
    idx += 2

intervals.sort()

merged = []
for interval in intervals:
    L, R = interval
    if not merged:
        merged.append([L, R])
    else:
        last_L, last_R = merged[-1]
        if L <= last_R:
            merged[-1][1] = max(last_R, R)
        else:
            merged.append([L, R])

for interval in merged:
    print(interval[0], interval[1])

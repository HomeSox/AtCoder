N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
S = input()

Y = [x[1] for x in XY]

search = {}
for y in set(Y):
    search[y] = {
        'R': 10**10,
        'L': -1,
    }

for i, s in enumerate(S):
    x, y = XY[i]

    if s == 'R':
        search[y]['R'] = min(search[y]['R'], x)
        continue

    if s == 'L':
        search[y]['L'] = max(search[y]['L'], x)
        continue

for y in set(Y):
    if search[y]['L'] >= search[y]['R']:
        print('Yes')
        exit()

print('No')

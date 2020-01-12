N, M = map(int, input().split())


ans_d = {}

cnt_d = {}

for i in range(N):
    cnt_d[i+1] = 0

for i in range(M):
    p, s = input().split()
    if int(p) in ans_d: continue
    if s == 'AC':
        ans_d[int(p)] = cnt_d[int(p)]
    elif s == 'WA':
        cnt_d[int(p)] += 1


ans = 0
for k, v in ans_d.items():
    ans += v


print('{} {}'.format(len(ans_d), ans))

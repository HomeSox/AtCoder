N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

newxy = []
cur = 0 if xy[0][0] == 1 else 1
for xy_ in xy:
    if xy_[0] == cur:
        if xy_[0] == 0:
            newxy[-1][1] = max(newxy[-1][1], newxy[-1][1] + xy_[1])
        else:
            newxy[-1][1] = max(newxy[-1][1], xy_[1])
    else:
        newxy.append(xy_)
        cur = xy_[0]

for x, y in newxy:
    print(x, y)


dp = [0 for _ in range(len(newxy))]

dp[0] = max(0, newxy[0][1])
dp[1] = max(dp[0], dp[0] + newxy[1][1]) if newxy[1][0] == 0 else newxy[1][1]

is_choice_1 = True if newxy[1][0] == 0 else False
for i in range(2, len(newxy)):
    if newxy[i][0] == 0:  # if the current state is 0
        dp[i] = max(dp[i - 1], dp[i - 1] + newxy[i][1])

        is_choice_1 = True if dp[i - 1] + newxy[i][1] >= dp[i - 1] else False
    else:  # if the current state is 1
        if is_choice_1:
            dp[i] = max(dp[i - 1], dp[i - 1] + newxy[i][1])

            is_choice_1 = True if dp[i - 1] + newxy[i][1] > dp[i - 1] else False
        else:
            dp[i] = dp[i - 1]

print(dp)
print(max(dp))

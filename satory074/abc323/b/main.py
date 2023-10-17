N = int(input())

wins = [[i + 1, 0] for i in range(N)]
for i in range(N):
    S = input()
    for j, s in enumerate(S):
        if s == 'o':
            wins[i][1] += 1

wins.sort(key=lambda x: x[1], reverse=True)

ans = []
for idx, c in wins:
    ans.append(idx)

print(*ans)
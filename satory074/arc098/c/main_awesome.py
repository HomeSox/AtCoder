N = int(input())
S = input()

qW = [0 for _ in range(N)]
qE = [0 for _ in range(N)]
for i, s in enumerate(S):
    qW[i] = qW[i - 1] + (1 if s == "W" else 0)
    qE[i] = qE[i - 1] + (1 if s == "E" else 0)

ans = 10**9
for i, s in enumerate(S):
    l_west = qW[i - 1] if i else 0
    r_east = qE[-1] - qE[i]

    ans_ = l_west + r_east
    if ans_ < ans:
        ans = ans_

print(ans)

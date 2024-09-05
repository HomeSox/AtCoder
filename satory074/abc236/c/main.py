N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

cur = 0
for i, s in enumerate(S):
    if s == T[cur]:
        print("Yes")
        cur += 1
    else:
        print("No")

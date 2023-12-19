N = int(input())
S = input()

ans = 0

for flip in range(2):
    level = 0
    for i in range(N):
        if S[i] == '-':
            ans = max(ans, level)
            level = 0
        else:
            level += 1
    
    S = S[::-1]

if ans:
    print(ans)
else:
    print(-1)

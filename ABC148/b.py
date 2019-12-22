N = int(input())
S, T = input().split()

ans = ''
for i in range(N):
    ans += S[i:i+1] + T[i:i+1]

print(ans)

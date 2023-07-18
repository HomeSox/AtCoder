N = int(input())

ans = (N // 10) * 100
ans += min((N % 10) * 15, 100)

print(ans)

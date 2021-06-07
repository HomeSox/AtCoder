n, a, b = map(int, input().split())

ans = 0
for i in range(n+1):
    sum_ = sum(map(int, list(str(i))))
    if a <= sum_ <= b:
        ans += i

print(ans)
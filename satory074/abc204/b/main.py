n = int(input())
a = list(map(int, input().split()))

ans = 0
for a_ in a:
	ans += max(a_-10, 0)
print(ans)
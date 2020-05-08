H = int(input())

cnt = 0

for i in range(1, 40):
    if 2**i <= H: cnt += 1


ans = 0
for i in range(cnt+1):
    ans += pow(2, i)

print(ans)

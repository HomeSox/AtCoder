N = int(input())
AC = [list(map(int, input().split())) + [i + 1] for i in range(N)]

AC.sort(key=lambda x: (x[0], x[1]))

min_c = float('inf')
ans = []

for a, c, index in reversed(AC):
    if min_c >= c:
        min_c = c
        ans.append(index)

ans.sort()
print(len(ans))
print(*ans)

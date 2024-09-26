import itertools

M = int(input())
ans = []
for i in range(11):
    ans += [i] * (M % 3)
    M //= 3

print(len(ans))
print(*ans)

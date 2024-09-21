n = int(input())
a = list(map(int, input().split()))

ans = []
for i, a_ in enumerate(a):
    if i % 2 == 0:
        ans.append(a_)
    else:
        ans.insert(0, a_)

if n % 2 == 1:
    ans = ans[::-1]

print(*ans)

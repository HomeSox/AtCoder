N = int(input())
a = list(map(int, input().split()))

n = 0
for a_ in a:
    n ^= a_

ans = [n ^ a_ for a_ in a]
print(*ans)

N = int(input())
h = list(map(int, input().split()))

ans = 0
h1 = 0
for h_ in h:
    if h_ > h1:
        ans += h_ - h1

    h1 = h_

print(ans)

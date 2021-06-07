n = int(input())
a = list(map(int, input().split()))

ans = 0
for a_ in a:
    if a_ % 2 == 0:
        a_ = a_ / 2
    else:
        break



n = int(input())
a = list(map(int, input().split()))

ans = 0
is_proc = True

while is_proc:
    for a_ in a:
        if a_ % 2 == 0:
            a_ = a_ / 2
        else:
            is_proc = False
            break

    ans += 1

print(ans)


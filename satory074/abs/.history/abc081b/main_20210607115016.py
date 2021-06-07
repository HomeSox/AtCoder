n = int(input())
a = list(map(int, input().split()))

ans = 0
is_proc = True

while is_proc:
    for i, a_ in enumerate(a):
        if a_ % 2 == 0:
            a[i] = a_ / 2
        else:
            is_proc = False
            break
    else:
        ans += 1

print(ans)


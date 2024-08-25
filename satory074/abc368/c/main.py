N = int(input())
H = list(map(int, input().split()))

t = 0
for h in H:
    q, r = divmod(h, 5)

    t += q * 3
    h -= q * 5
    while h > 0:
        t += 1

        if t % 3 == 0:
            h -= 3
        else:
            h -= 1

    # print(q, r)

print(t)

A, B, C = map(int, input().split())

now = B
while now != C:
    if now == A:
        print("No")
        exit()

    now += 1
    now %= 24

print("Yes")

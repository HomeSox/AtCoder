X = int(input())

ans = 1
for i in range(1, 10 ** 18):
    if ans == X:
        print(i)
        exit()

    ans *= (i + 1)


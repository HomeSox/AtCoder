N = int(input())
l = list([input() for _ in range(N)])

cur = l[0]
for i, l_ in enumerate(l[1:]):
    print(i, cur)

    if l_ == cur:
        if i == N - 2:
            print("Yes")
            exit()

        print("No")
        exit()
    else:
        cur = l_

print("Yes")

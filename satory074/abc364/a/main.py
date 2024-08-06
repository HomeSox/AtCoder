N = int(input())
l = list([input() for _ in range(N)])

cur = l[0]
for i, l_ in enumerate(l[1:-1]):
    # print(i, cur)

    if l_ == cur and l_ == "sweet":
        print("No")
        exit()

    cur = l_

print("Yes")

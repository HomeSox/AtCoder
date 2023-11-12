B = int(input())

if B == 1:
    print(1)
    exit()

for i in range(10 ** 7):
    if i ** i == B:
        print(i)
        exit()

    if i ** i > 10 ** 18:
        break

print(-1)
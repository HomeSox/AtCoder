N = int(input())

for x in range(10 ** 3):
    for y in range(10 ** 3):
        if (2 ** x) * (3 ** y) == N:
            print('Yes')
            exit()

print('No')

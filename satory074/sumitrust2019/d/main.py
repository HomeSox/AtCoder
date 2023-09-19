N = int(input())
S = input()

ans = 0
for i in range(1000):
    key = str(i).zfill(3)

    n1 = S.find(key[0])

    if n1 == -1:
        continue

    n2 = S.find(key[1], n1 + 1)
    if n2 == -1:
        continue

    n3 = S.find(key[2], n2 + 1)
    if n3 == -1:
        continue

    ans += 1

print(ans)

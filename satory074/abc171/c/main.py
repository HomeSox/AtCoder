N = int(input())

k = 1
total = 0
while True:
    total += 26**k

    if N <= total:
        break

    k += 1


total -= 26**k
pos = N - total - 1

name = []
for _ in range(k):
    name.append(chr(ord("a") + pos % 26))
    pos //= 26

name = "".join(reversed(name))

print(name)

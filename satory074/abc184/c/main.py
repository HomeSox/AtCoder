r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r = r2 - r1
c = c2 - c1

if (r, c) == (0, 0):
    exit(print(0))

if r == c or r == -c:
    exit(print(1))

if abs(r) + abs(c) <= 3:
    exit(print(1))

if (r ^ c ^ 1) & 1:
    exit(print(2))

if abs(r) + abs(c) <= 6:
    exit(print(2))

if abs(r + c) <= 3 or abs(r - c) <= 3:
    exit(print(2))

print(3)

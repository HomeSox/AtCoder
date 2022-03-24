import collections as cl

A, B, C = map(int, input().split())

ans = A * B * C

a = abs(((A // 2) * B * C) - ((A - A // 2) * B * C))
b = abs(((B // 2) * A * C) - ((B - B // 2) * A * C))
c = abs(((C // 2) * B * A) - ((C - C // 2) * B * A))

print(min([a, b, c]))

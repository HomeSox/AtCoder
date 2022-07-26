x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

if x1 + r < x2 or x1 + r > x3 or y1 - r < y2 or y1 + r > y3:
    print("YES")
else:
    print("NO")

if (
    (x2 - x1) ** 2 + (y2 - y1) ** 2 > r ** 2
    or (x2 - x1) ** 2 + (y3 - y1) ** 2 > r ** 2
    or (x3 - x1) ** 2 + (y2 - y1) ** 2 > r ** 2
    or (x3 - x1) ** 2 + (y3 - y1) ** 2 > r ** 2
):
    print("YES")
else:
    print("NO")

a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for ai in range(a+1):
    for bi in range(b+1):
        for ci in range(c+1):
            if ai * 500 + bi * 100 + ci * 50:
                ans += 1

print(ans)

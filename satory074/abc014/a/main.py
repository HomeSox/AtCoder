a = int(input())
b = int(input())

if a > b:
    print(b - (a % b))
else:
    print(b - a)
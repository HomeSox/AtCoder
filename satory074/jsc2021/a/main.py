X, Y, Z = map(int, input().split())

answer = (Z / X) * Y

if answer.is_integer():
    print(int(answer) - 1)
else:
    print(int(answer))
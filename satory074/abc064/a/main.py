r, g, b = map(str, input().split())

n = int(f'{r}{g}{b}')
if n % 4 == 0:
    print('YES')
else:
    print('NO')

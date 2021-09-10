X = list(map(int, list(input())))

if len(set(list(X))) == 1:
    print('Weak')
    exit()

for x1, x2 in zip(X[:-1], X[1:]):
    if (10 if x2 == 0 else x2) - x1 == 1:
        None
    else:
        break
else:
    print('Weak')
    exit()

print('Strong')
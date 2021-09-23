T = int(input())
for _ in range(T):
    case = int(input())
    if case % (2 ** 2) == 0:
        print('Even')
    elif case % (2 ** 1) == 0:
        print('Same')
    else:
        print('Odd')
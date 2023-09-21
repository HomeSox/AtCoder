S = input()

for i, s in enumerate(S):
    if i % 2 == 0:
        if s == 'R' or s == 'U' or s == 'D':
            continue
        else:
            print('No')
            exit()
    else:
        if s == 'L' or s == 'U' or s == 'D':
            continue
        else:
            print('No')
            exit()

print('Yes')

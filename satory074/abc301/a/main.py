N = int(input())
S = input()

cur = S[0]
t = S.count('T')
a = S.count('A')

if t != a:
    if t > a:
        print('T')
    else:
        print('A')

    exit()

ans = t
t = 0
a = 0
for s in S:
    if s == 'T':
        t += 1
    else:
        a += 1

    if t == ans:
        print('T')
        exit()

    if a == ans:
        print('A')
        exit()
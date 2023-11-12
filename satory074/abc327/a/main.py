N = int(input())
S = input()

for s1, s2 in zip(S[:-1], S[1:]):
    if s1 == 'a' and s2 == 'b':
        print('Yes')
        exit()

    if s1 == 'b' and s2 == 'a':
        print('Yes')
        exit()

print('No')

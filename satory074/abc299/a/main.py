N = int(input())
S = input()

ans =''
for s in S:
    if s == '.':
        continue

    ans += s

if ans == '|*|':
    print('in')
else:
    print('out')

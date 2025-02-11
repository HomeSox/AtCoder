S = input()

ans = ''

for s in S:
    if s == '0':
        ans += '0'
    elif s == '1':
        ans += '1'
    else:
        if ans != '':
            ans = ans[:-1]

print(ans)


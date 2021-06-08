s = input()

for s_ in list(s)[::-1]:
    otpt = s_
    if s_ == '6':
        otpt = '9'

    if s_ == '9':
        otpt = '6'

    print(s_, end='')
print()
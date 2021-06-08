s = input()

for s_ in list(s)[:-1]:
    if s_ == '6':
        s_ = '9'

    if s_ == '9':
        s_ = '6'

    print(s_, end='')
print()
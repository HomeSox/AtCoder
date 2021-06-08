s = input()

for s_ in list(s):
    if s_ == '6':
        s_ = '9'

    if s_ == '9':
        s_ = '6'

    print(s_, end='')
s  = input()
n  = int(input())

s_mae = ''
s_ato = s

for _ in range(n):
    ipt = input()

    if ipt[0] == '1':
        s_mae, s_ato = s_ato, s_mae
    else:
        _, id_, s_ = ipt.split()
        is_head = True if id_ == '1' else False
        if is_head:
            s_mae += s_
        else:
            s_ato += s_

print(s_mae[::-1] + s_ato)

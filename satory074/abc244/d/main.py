S = list(input().split())
T = list(input().split())

S = ''.join(S)
T = ''.join(T)

g1 = ['RGB', 'GBR', 'BRG']
g2 = ['RBG', 'GRB', 'BGR']

if S in g1:
    if T in g1:
        print('Yes')
    else:
        print('No')
else:
    if T in g2:
        print('Yes')
    else:
        print('No')


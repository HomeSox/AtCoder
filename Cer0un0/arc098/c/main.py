#!/usr/bin/env python3

N = int(input())
S = input()

P = [0 for i in range(N)]

w_c = S.count('W')
e_c = S.count('E')
if S[0] == 'W':
    P[0] = {'W_l':0, 'W_r':w_c-1, 'E_l':0, 'E_r':e_c}
else:
    P[0] = {'W_l':0, 'W_r':w_c, 'E_l':0, 'E_r':e_c-1}


for i in range(1, N):
    b = P[i-1]
    if S[i] == 'W':
        if S[i-1] == 'W':
            P[i] = {'W_l':b['W_l']+1, 'W_r':b['W_r']-1, 'E_l':b['E_l'], 'E_r':b['E_r']}
        else:
            P[i] = {'W_l':b['W_l'], 'W_r':b['W_r']-1, 'E_l':b['E_l']+1, 'E_r':b['E_r']}

    else: # S[i] == 'E'
        if S[i-1] == 'W':
            P[i] = {'W_l':b['W_l']+1, 'W_r':b['W_r'], 'E_l':b['E_l'], 'E_r':b['E_r']-1}
        else:
            P[i] = {'W_l':b['W_l'], 'W_r':b['W_r'], 'E_l':b['E_l']+1, 'E_r':b['E_r']-1}


ans = 10**9
for i in range(N):
    ans = min(P[i]['W_l']+P[i]['E_r'], ans)
print(ans)

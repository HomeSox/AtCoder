N, K = map(int, input().split())
R2, S, P = map(int, input().split())
T = input()

R = []

for i in range(K):
    if T[i]=='r':
        R.append('p')
    elif T[i]=='s':
        R.append('r')
    else:
        R.append('s')

for i in range(K, len(T)):
    if T[i]=='r':
        if R[i-K] == 'p':
            R.append('x')
        else:
            R.append('p')
    elif T[i]=='s':
        if R[i-K] == 'r':
            R.append('x')
        else:
            R.append('r')
    else:
        if R[i-K] == 's':
            R.append('x')
        else:
            R.append('s')

ans = 0
for r in R:
    if r=='p': ans += P
    elif r=='r': ans += R2
    elif r=='s': ans += S

print(ans)




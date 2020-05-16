#!/usr/bin/env python3

S = input()
K = int(input())

if len(S) == 1:
    print(K//2)
    exit()

A = []
cnt = 1
C = []
for i in range(1,len(S)):
    if S[i-1] == S[i]:
        cnt += 1
    else:
        C.append([S[i-1], cnt])
        cnt = 1
C.append([S[i], cnt])

ans = 0
S2 = []
for c in C:
    ans += (c[1])//2
    if c[1] == 1:
        S2.append(False)
    else:
        for i in range(c[1]):
            if i % 2 == 1:
                S2.append(True)
            else:
                S2.append(False)

ans *= K

ans2 = 0
if S[0] == S[-1]:
    if S2[-1] == False and S2[0] == True:
        ans2 = K //2
    elif S2[-1] == False and S2[0] == False:
        ans2 = K-1

print(S)
print(S2)
print(K)
print(C)

print('ans', ans)
print('ans2', ans2)


print(ans + ans2)

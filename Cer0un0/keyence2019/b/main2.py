#!/usr/bin/env python3

S = input()
key = 'keyence'
K = []

for i in range(len(key)+1):
    K.append([key[:i],key[i:]])

S = S[S.find('k'):]

#print(K)
for i in range(len(K)):
    if K[i][0] in S and K[i][1] in S:
        print('YES')
        exit()
print('NO')

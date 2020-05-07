#!/usr/bin/env python3
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N, P = map(int, input().split())

F = factorization(P)
numbers = []
ans = 1
for i in range(len(F)):
    if F[i][1] >= N: ans *= F[i][0] ** (F[i][1]//N)


print(ans)

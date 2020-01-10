import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = [i for i in range(1, N+1)]

C = list(itertools.permutations(R, N))

a = 0
b = 0
for i in range(len(C)):
    if list(C[i]) == P: a = i
    if list(C[i]) == Q: b = i

print(abs(a-b))


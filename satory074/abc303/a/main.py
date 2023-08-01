import collections as cl
import math

N = int(input())
S = input()
T = input()

for s, t in zip(S, T):
    if s == t:
        continue

    if s == '1' and t == 'l':
        continue

    if s == 'l' and t == '1':
        continue

    if s == '0' and t == 'o':
        continue

    if s == 'o' and t == '0':
        continue

    break
else:
    print('Yes')
    exit()

print('No')


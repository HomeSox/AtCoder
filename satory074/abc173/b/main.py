import collections as cl
import math

N = int(input())
S = [input() for _ in range(N)]

clc = cl.Counter(S)

print(f'AC x {clc["AC"]}')
print(f'WA x {clc["WA"]}')
print(f'TLE x {clc["TLE"]}')
print(f'RE x {clc["RE"]}')

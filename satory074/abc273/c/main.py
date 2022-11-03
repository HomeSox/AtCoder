import collections as cl
import math

N = int(input())
A = list(map(int, input().split()))

clc = cl.Counter(A)

numbers = list(clc.keys())
numbers.sort()

number2index = {n: i for i, n in enumerate(numbers)}
dict_ = {n: 0 for n in numbers}

for n in numbers:
    dict_[n] = len(numbers) - number2index[n] - 1

alterdict_ = {i: 0 for i in range(N)}
for k, v in dict_.items():
    alterdict_[v] = clc[k]

for i in range(N):
    print(alterdict_[i])

# print(numbers)
# print(dict_)
# print(alterdict_)

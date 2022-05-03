import collections as cl
import math

N = int(input())

s = []
t = []
for _ in range(N):
    s_, t_ = input().split()

    s.append(s_)
    t.append(t_)

for i in range(N):
    is_ok_sei = True
    is_ok_mei = True

    for j in range(N):
        if i == j:
            continue

        if s[i] == s[j] or s[i] == t[j]:
            is_ok_sei = False

        if t[i] == s[j] or t[i] == t[j]:
            is_ok_mei = False

    if is_ok_sei or is_ok_mei:
        pass
    else:
        print("No")
        break
else:
    print("Yes")

import collections as cl
import math

N, M = map(int, input().split())
name = input()
kit = input()

name_dict = cl.Counter(name)
kit_dict = cl.Counter(kit)

ans = 0
for i in name_dict.keys():
    if i not in kit_dict.keys():
        ans = -1
        break
    else:
        ans = max(ans, math.ceil(name_dict[i] / kit_dict[i]))

print(ans)

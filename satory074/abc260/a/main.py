import collections as cl
import math
import collections as cl

S = input()

clc = cl.Counter(S)
if clc.most_common()[-1][1] == 1:
    print(clc.most_common()[-1][0])
else:
    print(-1)

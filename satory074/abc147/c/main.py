#!/usr/bin/env pypy3
import collections
import itertools as it
import math
#import numpy as np
 
n  = int(input())
#  = int(input())
#  = map(int, input().split())
#  = list(map(int, input().split()))i
xy = []
for _ in range(n):
    a = int(input())
    xy.append([tuple(map(int, input().split())) for _ in range(a)])
#
# c = collections.Counter()

for i in range(2 ** n): # 嘘つき・正直者の総当り
    is_honest = [not(bool(int(s))) for s in list(f'{i:015b}'[-n:])]
    is_ok = True
    for i, h in enumerate(list(is_honest)): # 人の総当り
        for x, y in xy[i]: # 証言の総当り
            if is_honest[i] == False:
                continue

            x = x - 1
            v = bool(int(y))
            
            #print(is_honest[x], bool(y), v, )
            if is_honest[x] == v:
                pass
            else:
                is_ok = False
    
    if is_ok:
        i#print(is_honest)
        print(sum(is_honest))
        break

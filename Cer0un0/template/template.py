#!/usr/bin/env python3

MOD = 10**9

#-------------
# 約数
#-------------

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

#-------------
# 素因数分解
#-------------
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


#-------------
# 入力
#-------------

N = int(input())
S = input()
a, b = map(int, input().split())
A = list(map(int, input().split()))
B = [int(input()) for i in range(N)]
d = [0 for i in range(N)]

#-------------
# 出力
#-------------
print(' '.join(map(str, A))) #配列をスペース区切りで出力

#-------------
# 文字連結
#-------------
print(''.join(A)) #リストAの中身を文字連結(strのとき)

#-------------
# ビット演算
#-------------
l = [f'{i:015b}' for i in range(N)]

#----

from itertools import product
[print(p) for p in product([0,1], repeat=3)]
for p in product([0,1], repeat=3):
    pass


#古いpython
l = list('{:015b}'.format(N))


#-------------
#優先度付きキュー
#-------------

import heapq
#最大値を取るとき マイナスになっているので注意
A = list(map(lambda x: x*(-1), A))  # 各要素を-1倍
heapq.heapify(list)
MAX = heapq.heappop(A)

#最小値を取るとき
heapq.heapify(list)
MIN = heapq.heappop(A)

#値を入れる
heapq.heappush(list, VALUE)



#-------------
# Deque
#-------------

from collections import deque
que = deque(list)
que.popleft() # 左の要素を取り出す
que.append(V) # 右に要素を追加
que.appendleft(V) # 左に要素を追加


#-------------
# LCM 最小公倍数
#-------------

import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

# 旧
import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

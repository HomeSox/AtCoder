#!/usr/bin/env python3

S = input()

player = '''tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481'''

name_rate = {}
for p in player.split('\n'):
    name, rate = p.split(' ')
    if name == S:
        print(rate)
        exit()

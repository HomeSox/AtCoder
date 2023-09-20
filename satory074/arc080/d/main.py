H, W = list(map(int, input().split()))
N = int(input())
a = list(map(int, input().split()))

l = []
for i, a_ in enumerate(a):
    l += [i + 1] * a_

# lをW個ずつに分割
l = [l[i:i+W] for i in range(0, len(l), W)]
for i, l_ in enumerate(l):
    if i % 2 == 1:
        l_ = l_[::-1]
    print(*l_, sep=' ')

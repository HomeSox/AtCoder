N = int(input())
p = list(map(int, input().split()))

q = [0 for _ in range(N)]
for i, p_ in enumerate(p):
    q[p_-1] = i + 1

print(' '.join(list(map(str, q))))
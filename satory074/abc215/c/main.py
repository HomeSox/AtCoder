import itertools

S, K_ = input().split()
K = int(K_)

order = sorted(list(set(itertools.permutations(S))))
print(''.join(order[K-1]))
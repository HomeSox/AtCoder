from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

def is_1moji_chigai(w1, w2):
    if len(w1) != len(w2):
        return False
    
    diff = 0
    for s1, s2 in zip(w1, w2):
        if s1 == s2:
            continue
        
        diff += 1
        if diff > 1:
            return False
    
    return diff == 1

for perm in permutations(S):
    for w1, w2 in zip(perm[:-1], perm[1:]):
        if is_1moji_chigai(w1, w2):
            continue
        else:
            break
    else:
        print('Yes')
        exit()

print('No')

import itertools

N = int(input())
R = input()
C = input()

for a in itertools.permutations(range(N)):
    for b in itertools.permutations(range(N)):
        for c in itertools.permutations(range(N)):
            is_valid = True
            for ai, bi, ci in zip(a, b, c):
                if ai == bi or bi == ci or ci == ai:
                    is_valid = False
                    break

            if not is_valid:
                continue

            S = [["." for _ in range(N)] for _ in range(N)]

            for i, j in enumerate(a):
                S[i][j] = "A"

            for i, j in enumerate(b):
                S[i][j] = "B"

            for i, j in enumerate(c):
                S[i][j] = "C"

            # R
            r = ''
            for srow in S:
                for s in srow:
                    if s == '.':
                        continue

                    r += s
                    break

            # C
            c_ = ''
            for srow in list(zip(*S)):
                for s in srow:
                    if s == '.':
                        continue

                    c_ += s
                    break

            if r == R and c_ == C:
                print('Yes')

                for srow in S:
                    print(''.join(srow))

                exit()

print('No')
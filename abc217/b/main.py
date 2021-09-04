S = [input() for _ in range(3)]
S_ = ['ABC', 'ARC', 'AGC', 'AHC']
for s in S_:
    if not s in S:
        print(s)
        break
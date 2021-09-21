X = input()
N = int(input())
S = [input() for _ in range(N)]
S = sorted(S, key=lambda x: [X.index(c) for c in x])
[print(i) for i in S]
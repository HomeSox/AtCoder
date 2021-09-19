X = list(input())
N = int(input())
# S = [input() for _ in range(N)]

# print(ord('z'), ord('A'))
S = []
for _ in range(N):
    w = ''
    for s in list(input()):
        w += X[ord(s) - 97]
    # print(w)

    S.append(w)

S.sort()
# print()

for s in S:
    w = ''
    for s_ in list(s):
        w += chr(X.index(s_) + 97)

    print(w)

print(chr(0+97))

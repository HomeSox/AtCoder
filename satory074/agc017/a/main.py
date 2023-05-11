N, P = map(int, input().split())
A = list(map(int, input().split()))

odd = [a for a in A if a & 1]

if odd:
    print(2 ** (N - 1))
else:
    if P == 0:
        print(2 ** N)
    else:
        print(0)

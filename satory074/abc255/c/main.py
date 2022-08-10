X, A, D, N = map(int, input().split())

if D < 0:
    fi = A + D * (N - 1)
    A = fi
    D *= -1

fi = A + D * (N - 1)
st = A

if st <= X <= fi:
    m = 0 if X == 0 else (X - st) % D

    exit(print(min(m, D - m)))
elif X < st:
    exit(print(st - X))
else:
    exit(print(X - fi))

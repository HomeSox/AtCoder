N = int(input())
A = list(map(int, input().split()))

Q = int(input())
all_ = None
delta = [0] * N
idxs = set(range(N))

for _ in range(Q):
    query = input().split()

    if query[0] == "1":
        x = int(query[1])
        all_ = x

        for idx in idxs:
            delta[idx] = 0

        idxs.clear()

    elif query[0] == "2":
        i = int(query[1]) - 1
        x = int(query[2])

        if all_ is None:
            A[i] += x
        else:
            delta[i] += x
            idxs.add(i)

    elif query[0] == "3":
        i = int(query[1]) - 1
        if all_ is None:
            print(A[i])
        else:
            print(all_ + delta[i])

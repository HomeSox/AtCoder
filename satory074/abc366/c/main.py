from collections import defaultdict

Q = int(input())

bag = defaultdict(int)
dict_ = set()

for _ in range(Q):
    query = input().split()

    if query[0] == "1":
        x = int(query[1])
        bag[x] += 1
        dict_.add(x)

    elif query[0] == "2":
        x = int(query[1])
        bag[x] -= 1
        if bag[x] == 0:
            dict_.remove(x)

    elif query[0] == "3":
        print(len(dict_))

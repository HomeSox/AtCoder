Q = int(input())

l = [0 for _ in range(100)]
for i in range(Q):
    query = input()

    if query[0] == '1':
        x = int(query.split()[1])
        l.append(x)
    else:
        print(l.pop())

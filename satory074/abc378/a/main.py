from collections import Counter

A = list(map(int, input().split()))

c = Counter(A)
mc = c.most_common()[0]

if mc[1] == 4:
    print(2)
else:
    mc2 = c.most_common()[1]

    if mc[1] == mc2[1] == 2:
        print(2)
    else:
        if mc[1] >= 2:
            print(1)
        else:
            print(0)

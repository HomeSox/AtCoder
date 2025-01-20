l = list(map(int, input().split()))

l.sort()

if len(set(l)) == 1:
    print("Yes")
else:
    if l[0] + l[1] == l[2]:
        print("Yes")
    else:
        print("No")

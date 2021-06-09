n = int(input())

l = set()
for i in range(n):
    s = input()
    if s in l:
        pass
    else:
        l.add(s)
        print(i+1)


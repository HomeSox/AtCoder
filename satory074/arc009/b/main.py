b = list(map(int, input().split()))
N = int(input())

l = []
for i in range(N):
    a = input()

    s = ''
    for j in range(len(a)):
        s += str(b.index(int(a[j])))

    l.append([int(s), int(a)])

l.sort()

for i in range(N):
    print(l[i][1])



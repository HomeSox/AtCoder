A, B, C, D = map(int, input().split())

l = [A, 0]
for i in range(A):
    l[0] += B
    l[1] += C
    if l[0] <= l[1] * D:
        print(i + 1)
        break
else:
    print(-1)

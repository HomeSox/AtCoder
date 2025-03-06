N = int(input())
A = list(map(int, input().split()))

ans = 0
Q = []
for a in A:
    for i in range(len(Q)):
        Q[i] += a

    Q.append(a)

    # print(Q)

ans = 0
for q in Q:
    if q >= 4:
        ans += 1

print(ans)

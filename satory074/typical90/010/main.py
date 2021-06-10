n = int(input())
q1 = [0]
q2 = [0]
for _ in range(n):
    c, p = map(int, input().split())

    q1_ = p if c == 1 else 0
    q2_ = p if c == 2 else 0

    q1.append(q1[-1] + q1_)
    q2.append(q2[-1] + q2_)

# print(q1)
# print(q2)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print((q1[r] - q1[l-1]), (q2[r] - q2[l-1]))

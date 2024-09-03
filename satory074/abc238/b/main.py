N = int(input())
A = list(map(int, input().split()))

# 累積和
Q = [0]
for a in A:
    Q.append(Q[-1] + a)

Q2 = []
for q in Q[1:]:
    Q2.append(q % 360)

Q2.sort()
Q2 = [0] + Q2 + [360]

ans = []
for q1, q2 in zip(Q2[:-1], Q2[1:]):
    ans.append(q2 - q1)

# print(Q)
# print(Q2)
print(max(ans))

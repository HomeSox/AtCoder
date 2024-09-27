N = int(input())

sum_ = 0
for i in range(1, 10):
    for j in range(1, 10):
        sum_ += i * j

diff = sum_ - N

ans = []
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == diff:
            ans.append(str(i) + " x " + str(j))

ans.sort()

for a in ans:
    print(a)

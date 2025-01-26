N = int(input())
A = list(map(int, input().split()))

ball = []
count = 0

for a in A:
    count += 1
    if not ball or ball[-1][0] != a:
        ball.append([a, 1])
    else:
        ball[-1][1] += 1
        if ball[-1][1] == a:
            count -= a
            ball.pop()

    print(count)

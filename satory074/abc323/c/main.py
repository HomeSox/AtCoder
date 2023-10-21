N, M = map(int, input().split())
A = list(map(int, input().split()))

answers = []
for _ in range(N):
    answers.append(list(input()))

points = [0] * N
mada_task_point = [[] for _ in range(N)]
for i, a in enumerate(answers):
    p = i + 1

    for j, s in enumerate(answers[i]):
        if s == "o":
            p += A[j]
        else:
            mada_task_point[i].append(A[j])

    points[i] = p
    mada_task_point[i].sort(reverse=True)

# print(points)
# print(mada_task_point)

border_point = max(points)
# print(border_point)

for i, (mada, point) in enumerate(zip(mada_task_point, points)):
    diff = border_point - point

    c = 0
    for m in mada:
        if diff <= 0:
            print(c)
            break

        diff -= m
        c += 1
    else:
        print(c)

    # print(mada, point)

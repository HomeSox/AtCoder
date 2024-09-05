N = int(input())
A = list(map(int, input().split()))

fumidai = [0 for _ in range(N)]
for i, (a1, a2) in enumerate(zip(A[:-1], A[1:])):
    f = abs(a1 + fumidai[i] - a2)

    if a1 + fumidai[i] > a2:
        fumidai[i + 1] = f

# print(fumidai)
print(sum(fumidai))

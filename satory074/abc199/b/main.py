N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = [i for i in range(min(A), max(B) + 1)]
# print(ans)

for i in range(N):
    l = []
    for a in ans:
        if A[i] <= a <= B[i]:
            l.append(a)

    ans = l

print(len(ans))

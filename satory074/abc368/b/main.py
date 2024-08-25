N = int(input())
A = list(map(int, input().split()))

ans = 0
for _ in range(10**6):
    c = 0
    for a in A:
        if a > 0:
            c += 1
    # print(c)

    if c <= 1:
        break

    ans += 1

    A.sort(reverse=True)
    # print(A)

    A[0] -= 1
    A[1] -= 1

print(ans)

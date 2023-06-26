import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

sleep = {}
sleep = {0: 0}
total = 0
lidx = [0]
for i in range(1, len(A)):
    if i % 2 == 0:
        total += A[i] - A[i - 1]

    sleep[A[i]] = total
    lidx.append(A[i])

# print(sleep)
# print(lidx)

# print("---")
queries = []
for i in range(Q):
    ans = 0
    l, r = map(int, input().split())
    # print(l, r)

    left_idx = bisect.bisect_left(lidx, l)
    right_idx = bisect.bisect_right(lidx, r) - 1
    # print(left_idx, right_idx)

    if l != lidx[left_idx]:
        if sleep[lidx[left_idx]] != sleep[lidx[left_idx - 1]]:
            ans += lidx[left_idx] - l

    if r != lidx[right_idx]:
        if sleep[lidx[right_idx]] != sleep[lidx[right_idx + 1]]:
            ans += r - lidx[right_idx]

    ans += sleep[lidx[right_idx]] - sleep[lidx[left_idx]]

    # print(lidx[left_idx], lidx[right_idx - 1])

    # print(ans, lidx[left_idx] - l, r - lidx[right_idx])
    print(ans)

    # print()


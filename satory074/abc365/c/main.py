import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()

result = bisect.bisect_right(range(max(A)), M, key=lambda x: sum(min(x, a) for a in A))
print(result - 1)

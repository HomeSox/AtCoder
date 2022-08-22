N = int(input())

times = [0] * N
W = []
for i in range(N):
    T, K, *A = list(map(int, input().split()))
    times[i] = T
    W.append([a - 1 for a in A])

skill_tree = [False] * N
skill_tree[N-1] = True

ans = 0
for i in range(N-1, -1, -1):
    if skill_tree[i]:
        ans += times[i]
        for j in W[i]:
            skill_tree[j] = True

print(ans)

N, K, Q = map(int, input().split())

n_answer = [0 for _ in range(N + 1)]

for _ in range(Q):
    A = int(input())

    n_answer[A] += 1

# print(n_answer[1:])
max_ = max(n_answer[1:])
for i, n in enumerate(n_answer[1:]):
    if K - (Q - n) > 0:
        print('Yes')
    else:
        print('No')

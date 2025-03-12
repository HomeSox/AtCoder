N = int(input())
A = list(map(int, input().split()))

if N == 2:
    print("Yes")
    exit()

is_geometric = True
for i in range(1, N - 1):
    if A[i + 1] * A[0] != A[1] * A[i]:
        is_geometric = False
        break

print("Yes" if is_geometric else "No")

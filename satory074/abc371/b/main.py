N, M = map(int, input().split())
is_taro = [False for _ in range(N + 1)]

for _ in range(M):
    A, B = input().split()
    A = int(A)

    if B == "M" and (not is_taro[A]):
        is_taro[A] = True
        print("Yes")
    else:
        print("No")

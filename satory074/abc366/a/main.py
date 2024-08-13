N, T, A = list(map(int, input().split()))

rest = N - T - A

ans1 = "T" if T + rest > A else "A"
ans2 = "T" if T > A + rest else "A"

if ans1 == ans2:
    print("Yes")
else:
    print("No")

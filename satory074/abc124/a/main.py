A, B = map(int, input().split())

ans = 0
if A > B:
    ans += A
    A -= 1
else:
    ans += B
    B -= 1

if A > B:
    ans += A
else:
    ans += B

print(ans)

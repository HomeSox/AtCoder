A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

total= S + T
ans = S * A + T * B - total * (C if total >= K else 0)

print(ans)

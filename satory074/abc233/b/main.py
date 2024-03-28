L, R = map(int, input().split())
L -= 1
S = input()

print(f"{S[:L]}{S[L:R][::-1]}{S[R:]}")

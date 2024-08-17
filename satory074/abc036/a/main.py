A, B = map(int, input().split())

print(B // A + (0 if B % A == 0 else 1))

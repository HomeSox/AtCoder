def is_match(pattern, X, startX, startY):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == "#":
                if i + startX >= len(X) or j + startY >= len(X[0]) or X[i + startX][j + startY] != "#":
                    return False
    return True


def can_fit(A, B, X):
    for startX_A in range(len(X) - len(A) + 1):
        for startY_A in range(len(X[0]) - len(A[0]) + 1):
            if is_match(A, X, startX_A, startY_A):
                for startX_B in range(len(X) - len(B) + 1):
                    for startY_B in range(len(X[0]) - len(B[0]) + 1):
                        if is_match(B, X, startX_B, startY_B):
                            return "Yes"
    return "No"


HA, WA = map(int, input().split())
A = [list(input()) for _ in range(HA)]

HB, WB = map(int, input().split())
B = [list(input()) for _ in range(HB)]

HX, WX = map(int, input().split())
X = [list(input()) for _ in range(HX)]

print(can_fit(A, B, X))

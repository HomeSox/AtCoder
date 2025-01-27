A = list(map(int, input().split()))
AC = sorted(A)

possible = False
for i in range(len(A) - 1):
    temp_A = list(A)
    temp_A[i], temp_A[i + 1] = temp_A[i + 1], temp_A[i]
    if temp_A == AC:
        possible = True
        break

if possible:
    print("Yes")
else:
    print("No")

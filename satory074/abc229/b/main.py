A, B = map(int, input().split())

A = str(A).zfill(18)
B = str(B).zfill(18)

for a, b in zip(A, B):
    if int(a) + int(b) >= 10:
        print("Hard")
        break
else:
    print("Easy")

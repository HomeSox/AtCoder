N = int(input())
A = list(map(int, input().split()))

ma2 = sorted(A)[-2]

print(A.index(ma2) + 1)

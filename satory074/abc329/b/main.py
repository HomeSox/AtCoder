N = int(input())
A = list(map(int, input().split()))

l = sorted(list(set(A)))

print(l[-2])

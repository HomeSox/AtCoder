# = map(int, input())

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# AとBの排他的なリスト
l = list(set(A) ^ set(B))
l.sort()
print(*l)


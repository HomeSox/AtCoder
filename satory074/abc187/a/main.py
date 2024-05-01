A, B = map(str, input().split())

a = list(map(int, A))
b = list(map(int, B))

print(max(sum(a), sum(b)))


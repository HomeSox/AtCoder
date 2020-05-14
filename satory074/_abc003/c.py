n, k = map(int, input().split())
r = list(map(int, input().split()))

movie = sorted(r)[::-1][:k]
#print(movie)

c = 0
for m in movie[::-1]:
  c = (c + m) / 2
  
print(c)

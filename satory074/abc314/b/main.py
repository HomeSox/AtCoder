N = int(input())
C = []
A = []
for _ in range(N):
  c = int(input())
  a = list(map(int, input().split()))
  
  C.append(c)
  A.append(a)

X = int(input())

ans = []
cmin = 10 ** 18
for i, a in enumerate(A):
  if X in a:
    ans.append([C[i], i + 1])
    
    cmin = min(cmin, len(a))

ans.sort()

l = []
for c, i in ans:
  if c == cmin: 
    l.append(i)

print(len(l))
print(*l)

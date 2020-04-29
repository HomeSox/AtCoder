import collections as cl
n = int(input())
a = list(map(int, input().split()))

c = cl.Counter(a)

print(c[1])
for i, _ in enumerate(a):
  print(c[i+2])
N = int(input())
dic = {}

l = []
for _ in range(N):
  S = input()
  
  if len(S) == 1:
    S_ = S
  else:
    S_ = min(S, S[::-1])
  
  l.append(S_)

# print(l)
# print(set(l))
print(len(set(l)))

import collections as cl

S = input()
clc = cl.Counter(S)

ans, ma = clc.most_common()[0]
#print(clc.most_common())

for k, v in clc.most_common():
  if v == ma:
    if k < ans:
      ans = k
  else:
    break

print(ans)

  

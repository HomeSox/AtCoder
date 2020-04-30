import collections
 
n = int(input())
v = list(map(int, input().split()))
 
if len(set(v)) == 1:
  print(n//2)
else:
  v1 = v[::2]
  v2 = v[1::2]
  
  cmc1 = collections.Counter(v1).most_common()
  cmc2 = collections.Counter(v2).most_common()
  
  if cmc1[0][0] == cmc2[0][0]:    
    ans1 = (len(v1) - cmc1[0][1]) + (len(v2) - cmc2[1][1])
    ans2 = (len(v1) - cmc1[1][1]) + (len(v2) - cmc2[0][1])
    print(min(ans1, ans2))
  else:
    ans = (len(v1) - cmc1[0][1]) + (len(v2) - cmc2[0][1])
    print(ans)

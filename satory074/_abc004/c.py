n = int(input())

ordlist = ['123456']
for i in range(29):
  l = list(ordlist[-1])
  l[i%5], l[i%5+1] = l[i%5+1], l[i%5]
  
  ordlist.append(''.join(l))

print(ordlist[n%30])
  

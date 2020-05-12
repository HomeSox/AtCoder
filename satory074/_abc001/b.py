k = int(input()) / 1000

if k < 0.1:
  vv = '00'
elif 0.1 <= k <= 5:
  vv = '{:02}'.format(int(k*10))
elif 6 <= k <= 30:
  vv = str(k + 50)[:2]
elif 35 <= k <= 70:
  vv = '{:2}'.format(int((k - 30) / 5 + 80) * 10)[:2]
else:
  vv = '89'
  
print(vv)

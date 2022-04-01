A, B = map(int, input().split())

def n_uruu(n):
  ans = n // 4
  ans -= n // 100
  ans += n // 400
  
  return ans

print(n_uruu(B) - n_uruu(A-1))

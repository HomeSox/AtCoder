N, S, K = map(int, input().split())

sum_ = 0
for _ in range(N):
  P, Q = map(int, input().split())
  
  sum_ += P * Q

if sum_ >= S:
  print(sum_)
else:
  print(sum_ + K)

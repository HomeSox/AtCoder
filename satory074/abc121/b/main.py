N, M, C = map(int, input().split())
B = list(map(int, input().split()))

answer = 0
for _ in range(N):
   A = list(map(int, input().split()))

   sum_ = 0
   for a, b in zip(A, B):
       sum_ += a * b

   if sum_ + C > 0:
       answer += 1

print(answer)
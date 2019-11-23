N = int(input())
A = list(map(int, input().split()))

ans = 0
right = sum(A)
left = 0
for i in range(len(A)):
  right -= A[i]
  left += A[i]
  if left > right:
    break
ans1 = abs(left - right)
ans2 = abs((right + A[i]) -  (left - A[i]))

print(min(ans1, ans2))

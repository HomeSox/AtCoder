N = int(input())
A = list(map(int, input().split()))

# print(A)

min_ = 0
sum_ = 0
for a in A:
    sum_ += a
    min_ = min(min_, sum_)

print(sum_ + min_ * -1)

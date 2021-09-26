N = int(input())
A = list(map(int, input().split()))
X = int(input())

answer = N * (X // sum(A))
sum_ = sum(A) * (X // sum(A))

for a in A:
    if sum_ > X:
        break
    else:
        sum_ += a
        answer += 1

print(answer)

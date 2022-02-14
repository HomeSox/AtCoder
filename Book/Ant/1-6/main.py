n = int(input())
a = list(map(int, input().split()))


answer = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            len_ = a[i] + a[j] + a[k]
            ma = max(a[i], a[j], a[k])
            rest = len_ - ma

            if ma < rest:
                answer = max(answer, len_)

print(answer)

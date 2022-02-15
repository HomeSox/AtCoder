L = int(input())
n = int(input())
x = list(map(int, input().split()))

# min time
min_t = 0
for i in range(n):
    min_t = max(min_t, min(x[i], L - x[i]))

# max time
max_t = 0
for i in range(i):
    max_t = max(max_t, max(x[i], L - x[i]))

print(min_t)
print(max_t)

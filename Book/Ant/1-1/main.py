n = int(input())
m = int(input())
k = list(map(int, input().split()))

answer = 'No'
for i1 in range(n):
    for i2 in range(n):
        for i3 in range(n):
            for i4 in range(n):
                if k[i1] + k[i2] + k[i3] + k[i4] == m:
                    answer = 'Yes'

print(answer)
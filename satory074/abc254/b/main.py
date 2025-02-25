N = int(input())

row = [1]
print(*row)

for i in range(2, N+1):
    new_row = [1] * i
    for j in range(1, i-1):
        new_row[j] = row[j-1] + row[j]
    row = new_row
    print(*row)

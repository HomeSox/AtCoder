N = int(input())

names = []
ages = []
for _ in range(N):
    S, A = input().split()

    names.append(S)
    ages.append(int(A))

min_age = min(ages)
min_age_index = ages.index(min_age)

names = names[min_age_index:] + names[:min_age_index]

print(*names, sep="\n")

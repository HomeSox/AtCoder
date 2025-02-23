N = int(input())
l = [input() for _ in range(N)]
l = [[len(s), s] for s in l]

l.sort()

# print(l)

for _, s in l:
    print(s, end="")

print()

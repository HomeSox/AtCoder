S = input()
S = S.replace("ch", "a")

l = ["a", "o", "k", "u"]
for s in S:
    if s not in l:
        print("NO")
        exit()

# print(S)
print("YES")

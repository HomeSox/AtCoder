S = input()

if len(S) % 2 == 1:
    print("No")
    exit()

l = []
for i in range(0, len(S), 2):
    if S[i] in l:
        print("No")
        exit()

    if S[i] == S[i+1]:
        l.append(S[i])
    else:
        print("No")
        exit()

print("Yes")

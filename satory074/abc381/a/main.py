N = int(input())
S = input()

sp = S.split("/")
# print(sp, len(sp))


if len(sp) != 2:
    print("No")
    exit()

if len(list(sp[0])) != len(list(sp[1])):
    print("No")
    exit()

# print(sp, sp[0][0], sp[1][0])
if sp[0] == sp[1] == "":
    print("Yes")
else:
    if sp[0][0] == "1" and sp[1][0] == "2":
        print("Yes")
    else:
        print("No")

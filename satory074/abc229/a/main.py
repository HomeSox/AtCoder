S1 = input()
S2 = input()

if S1 == S2[::-1] and S1 != "##":
    print("No")
else:
    print("Yes")

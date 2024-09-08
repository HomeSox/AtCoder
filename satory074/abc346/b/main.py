W, B = map(int, input().split())

s = "wbwbwwbwbwbw" * 10**5

for i in range(len(s)):
    if s[i : i + W + B].count("w") == W and s[i : i + W + B].count("b") == B:
        print("Yes")
        exit()

print("No")

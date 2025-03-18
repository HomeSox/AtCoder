s = input()
chars = list(s)
i = 0

while i < len(chars) - 1:
    if chars[i] == "W" and chars[i + 1] == "A":
        chars[i] = "A"
        chars[i + 1] = "C"
        i = max(0, i - 1)
    else:
        i += 1

print("".join(chars))

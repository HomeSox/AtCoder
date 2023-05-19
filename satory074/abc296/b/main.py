ans = ''
for i in range(8):
    s = input()

    if '*' in s:
        ans += str(8 - i)
        ans += chr(ord('a') + s.index('*'))
        break

print(ans[::-1])

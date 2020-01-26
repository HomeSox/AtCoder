a, b = map(int, input().split())

A = str(a)*b
B = str(b)*a

s = [A, B]
s = sorted(s)
print(s[0])

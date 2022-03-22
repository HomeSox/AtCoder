N = int(input())
S = input()

left = []
right = []
for i, s in enumerate(S):
    if s == 'L':
        right.append(i)
    else:
        left.append(i)

print(*(left + [N] + right[::-1]))

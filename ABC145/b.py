N = int(input())
S = input()

for i in range(N):
    if S[:i] == S[i:]:
        print('Yes')
        exit()
print('No')

N = int(input())
S = input()

ma = [0 for _ in range(26)]

l = 0
while l < N:
    r = l + 1
    while r < N and S[l] == S[r]:
        r += 1

    c = ord(S[l]) - ord('a')
    ma[c] = max(ma[c], r - l)
    l = r

print(sum(ma))

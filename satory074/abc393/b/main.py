S = input()

ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        for k in range(j + 1, len(S)):
            if i == j or j == k or k == i:
                continue

            if S[i] == "A" and S[j] == "B" and S[k] == "C":
                if abs(i - j) == abs(j - k):
                    ans += 1
                    # print(i, j, k)

print(ans)

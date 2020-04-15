N = int(input())
S = input()

# 条件1だけを満たす組み合わせの数
ans = S.count('R') * S.count('G') * S.count('B')

# 条件2を満たさないものを、条件1でカウントしたものから減算
for l in range(N): # left
    for r in range(l+1, N): # right
        c = (r - l) // 2 + l # center
        if c - l == r - c: # 条件2を満たさない
            if len(set([S[l], S[c], S[r]])) == 3: # 条件1を満たす
                ans -= 1

print(ans)

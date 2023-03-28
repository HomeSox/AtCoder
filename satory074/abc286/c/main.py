import collections as cl
import math

N, A, B = map(int, input().split())
S = input()


def check(s):
    ans = 0
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            ans += 1
    return ans


ans = N * A * B
for i in range(N):
    s = S[i:] + S[:i]

    kouho = A * i + B * check(s)
    if kouho < ans:
        ans = kouho

    if A * i > ans:
        break

print(ans)

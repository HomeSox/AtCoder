#!/usr/bin/env python3

N, M = map(int, input().split())

'''
if N > 3 and M > 3:
    ans = N * M - 2*N - 2*M + 4
    print(ans)
'''

ans = N * M - 2*N - 2*M + 4
print(abs(ans))


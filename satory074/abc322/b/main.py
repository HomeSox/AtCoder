N, M = map(int, input().split())
S = input()
T = input()

is_stg_S = False
is_stg_T = False
if S == T[:N]:
    is_stg_S = True

if S == T[-N:]:
    is_stg_T = True

# print(S, T, T[:N], T[-N:])

if is_stg_S:
    if is_stg_T:
        print(0)
    else:
        print(1)
else:
    if is_stg_T:
        print(2)
    else:
        print(3)

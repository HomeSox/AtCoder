N = int(input())
A = list(map(int, input().split()))

is_exist_odd = False
for a in A:
    if a % 2 == 1:
        is_exist_odd = not is_exist_odd

print('NO' if is_exist_odd else 'YES')
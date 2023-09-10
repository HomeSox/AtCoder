N, M = map(int, input().split())
L = list(map(int, input().split()))


def check(w):
    n_line = 1
    n_line_length = 0
    for n_string_length in L:
        if n_line_length + n_string_length <= w:
            n_line_length += n_string_length + 1
        else:
            n_line += 1
            n_line_length = n_string_length + 1

    return n_line <= M


low = max(L)
high = sum(L) + (N - 1)
while low < high:
    mid = (low + high) // 2

    if check(mid):
        high = mid
    else:
        low = mid + 1

print(high)

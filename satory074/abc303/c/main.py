N, M, H, K = map(int, input().split())
S = input()
xy = {tuple(map(int, input().split())) for _ in range(M)}

visited = set()
curx, cury = 0, 0
for s in S:
    if s == 'R':
        curx += 1
    elif s == 'L':
        curx -= 1
    elif s == 'U':
        cury += 1
    elif s == 'D':
        cury -= 1

    H -= 1

    if H < 0:
        print('No')
        exit()

    cur = (curx, cury)
    if H < K and cur in xy and cur not in visited:
        H = K
        visited.add(current_pos)

print('Yes')

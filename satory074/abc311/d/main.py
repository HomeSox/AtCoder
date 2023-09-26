N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = [[False for _ in range(M)] for _ in range(N)]

start = (1, 1)
l = [start]
visited = set()

ans[start[0]][start[1]] = True

while l:
    y, x = l.pop()

    visited.add((y, x))

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        y_, x_ = y, x

        while 0 <= y_ < N and 0 <= x_ < M and S[y_][x_] != "#":
            ans[y_][x_] = True
            y_ += dy
            x_ += dx

        y__, x__ = (y_ - dy, x_ - dx)
        if 0 <= y__ < N and 0 <= x__ < M and (y__, x__) not in visited:
            l.append((y__, x__))

c = sum([row.count(True) for row in ans])
print(c)

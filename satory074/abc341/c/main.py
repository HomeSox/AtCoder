H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]

def is_ok(h, w):
    cur_w, cur_h = w, h
    for t in T:
        if t == 'L':
            cur_w -= 1
        elif t == 'R':
            cur_w += 1
        elif t == 'U':
            cur_h -= 1
        elif t == 'D':
            cur_h += 1

        if S[cur_h][cur_w] == "#":
            return False

    return True

ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue

        if is_ok(h, w):
            ans += 1

print(ans)

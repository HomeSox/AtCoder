N = int(input())
A = list(map(int, input().split()))
A = [0] + A

start = 1
l = [start]
visited = {start: 0}
while True:
    next = A[l[-1]]
    # print(next, l)
    if next in visited:
        idx = visited[next]
        print(len(l[idx:]))
        print(*l[idx:])
        exit()
    else:
        l.append(next)
        visited[next] = len(l) - 1

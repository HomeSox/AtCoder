N = int(input())
T = input()

ans = [0, 0]
state = 0
for t in T:
    if t == 'S':
        if state == 0:
            ans[0] += 1
        elif state == 1:
            ans[1] += -1
        elif state == 2:
            ans[0] += -1
        elif state == 3:
            ans[1] += 1
    else:
        state = (state + 1) % 4

print(ans[0], ans[1])
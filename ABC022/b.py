N = int(input())
d = {int(input()):1}
ans = 0
for i in range(N-1):
    a = int(input())

    if a in d and d[a] > 0:
        ans += 1
#        d[a] -= 1
    else:
        d.update({a: 1})

print(ans)

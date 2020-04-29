x, y, a, b, c = map(int, input().split())
red = list(map(int, input().split()))
gre = list(map(int, input().split()))
ino = list(map(int, input().split()))

red = sorted(red)[::-1]
gre = sorted(gre)[::-1]
ino = sorted(ino)[::-1]

eat = sorted(red[:x] + gre[:y])
ans = sum(eat)

for i in range(min(len(eat), len(ino))):
  if eat[i] < ino[i]:
    ans = ans - eat[i] + ino[i]
  else:
    break

print(ans)

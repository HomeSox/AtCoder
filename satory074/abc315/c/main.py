N = int(input())

FS = {}
for _ in range(N):
  f, s = map(int, input().split())
  if f not in FS:
    FS[f] = []
  FS[f].append(s)

res = 0
best = []
for f, scores in FS.items():
  scores.sort(reverse=True)
  if len(scores) >= 2:
    res = max(res, scores[0] + scores[1] // 2)
  if scores:
    best.append(scores[0])

best.sort(reverse=True)
if len(best) >= 2:
  res = max(res, best[0] + best[1])

print(res)

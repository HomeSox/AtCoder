mport collections

# A = input()
# A = int(input())
# A = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for i in range(N)]
#
# c = collections.Counter()
N = int(input())
S = [input() for s in range(N)]

c = collections.Counter(S)
cmc = c.most_common()
nmc = c.most_common()[0][1]

ans = []
for cmc_ in cmc:
  if cmc_[1] == nmc:
    ans.append(cmc_[0])
  else:
    break

ans.sort()
[print(ans_) for ans_ in ans]

N = int(input())
SC = [list(map(str, input().split())) for _ in range(N)]

SC.sort()

rate = 0
for s, c in SC:
  rate += int(c)

# print(rate)
# print(SC)
print(SC[rate % N][0])

import heapq

N, M, K = map(int, input().split())
t_sugar_water = [tuple(map(int, input().split())) for _ in range(N)]
a_sugar_water = [tuple(map(int, input().split())) for _ in range(M)]

# Sort sugar waters by concentration in descending order
t_sugar_water.sort(key=lambda x: x[0] / (x[0] + x[1]), reverse=True)
a_sugar_water.sort(key=lambda x: x[0] / (x[0] + x[1]), reverse=True)

l = []
ans_noudo = -1
for t_sugar, t_water in t_sugar_water:
    for a_sugar, a_water in a_sugar_water:
        sum_sugar = t_sugar + a_sugar
        sum_water = t_water + a_water

        noudo = sum_sugar / (sum_sugar + sum_water)

        if ans_noudo < 0:
            heapq.heappush(l, noudo)

            if len(l) == K:
                ans_noudo = l[0]
        else:
            ans_noudo = max(ans_noudo, noudo)

print(ans_noudo * 100)
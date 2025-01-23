N = int(input())

kashitsuki = 0
TV = []
for _ in range(N):
    T, V = map(int, input().split())
    TV.append([T, V])

for (t1, v1), (t2, v2) in zip(TV[:-1], TV[1:]):
    kashitsuki += v1
    kashitsuki -= t2 - t1
    kashitsuki = max(kashitsuki, 0)

kashitsuki += TV[-1][1]

print(kashitsuki)

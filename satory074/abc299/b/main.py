N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

color_ = T if T in C else C[0]

ans = 1
max_ = -1
for i in range(N):
  if C[i] == color_:
    if R[i] > max_:
      max_ = R[i]
      ans = i + 1

print(color_)
print(ans)

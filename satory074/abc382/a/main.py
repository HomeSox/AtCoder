N, D = map(int, input().split())
S = input()

kashibako = S.count("@")
kashibako -= D
print(N - max(kashibako, 0))

S = input()

l = ['Sunny', 'Cloudy', 'Rainy']
idx = l.index(S)
print(l[(idx + 1) % 3])

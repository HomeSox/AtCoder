D = input()

l = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

idx = l.index(D)
# print(idx, idx + 4, (idx + 4) % 8)
print(l[(idx + 4) % 8])

S = input()

l = []
for si in range(len(S)):
  for ei in range(si, len(S) + 1):
    st = S[si:ei]
    if st:
      l.append(st)

print(len(set(l)))

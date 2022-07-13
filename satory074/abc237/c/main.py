S = input()

_rstrip = S.rstrip("a")
lrstrip = _rstrip.lstrip("a")

n_ra = len(S) - len(_rstrip)
n_la = len(_rstrip) - len(lrstrip)

if lrstrip == lrstrip[::-1] and n_la <= n_ra:
    print("Yes")
else:
    print("No")

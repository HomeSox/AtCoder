N = int(input())
S = input()
Q = int(input())

dict_ = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}
for _ in range(Q):
    c, d = map(str, input().split())

    for k, v in dict_.items():
        if v == c:
            dict_[k] = d

ans = ""
for s in S:
    ans += dict_[s]

# print(dict_)
print(ans)

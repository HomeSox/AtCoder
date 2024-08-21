X = input()

ans = X.rstrip("0")

if ans[-1] == ".":
    print(ans[:-1])
else:
    print(ans)
"."

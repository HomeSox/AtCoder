N = int(input())
S = input()

ans = ""
is_inline = False
for s in S:
    if s == '"':
        is_inline = not is_inline

    if s == ',':
        if is_inline:
            ans += ','
        else:
            ans += '.'
    else:
        ans += s

    # print(is_inline, ans)

print(ans)

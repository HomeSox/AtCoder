A, B, X = map(int, input().split())
keta = [1,2,3,4,5,6,7,8,9,10]

uhen = {}
for k in keta:
    v = (X-B*k)//A
    if 10**k < v:
        v = 10**k-1
    elif v >= 10**k:
        v=10**k - 1
    uhen[k] = v

ans = 0
for k, v in uhen.items():
    if len(str(v)) == k:
        ans = max(ans, v)

if ans > 10**9: ans = 10**9
elif ans < 0 : ans = 0
print(ans)


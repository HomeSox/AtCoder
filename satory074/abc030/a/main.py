A, B, C, D = map(int, input().split())

if B / A == D / C:
    print("DRAW")
else:
    if B / A > D / C:
        print("TAKAHASHI")
    else:
        print("AOKI")

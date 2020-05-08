N = int(input())
A = list(map(int, input().split()))

B = [i for i in range(1,N+1)]

index = 0
ans = 0
for i in range(len(A)):
    if A[i] == B[index]:
        index += 1
    else:
        ans += 1

if index == 0:
    print('-1')
else:
    print(ans)

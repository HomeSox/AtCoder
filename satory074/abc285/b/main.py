N = int(input())
S = input()

for sa in range(1, N):
    ans = 0
    for st in range(N):
      if sa + st >= N:
        break
      
      if S[st] == S[st + sa]:
        break
      else:
        ans += 1
      
      # print(S[st], S[st+sa])
    
    print(ans)
    # print('--')
  

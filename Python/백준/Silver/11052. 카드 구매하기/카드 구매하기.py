N = int(input())
dp = [0]*(1001)
p = [0] + list(map(int,input().split()))
for i in range(1,N+1) :
    for j in range(1,i+1) :
        dp[i] = max(dp[i], dp[i-j]+p[j]) # j개 덜 샀을 때의 최대값과 더해서 비교
print(dp[N])
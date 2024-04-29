import sys
input = sys.stdin.readline
inf = sys.maxsize
n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [inf]*(k+1)
dp[0] = 0
for c in coin :
    for i in range(c,k+1) :
        dp[i] = min(dp[i],dp[i-c]+1)
if dp[k] == inf :
    print(-1)
else :
    print(dp[k])
import sys
input = sys.stdin.readline

T, W = map(int,input().split())
li = [int(input()) for _ in range(T)]
li = [0] + li
dp = [[0]*(W+1) for _ in range(T+1)] # 

dp[1][0] = li[1]%2
dp[1][1] = li[1]//2

for t in range(2,T+1) :
    for w in range(W+1) :
        if w%2 == 0 : #이동횟수 w가 짝수 : 1번 나무에 위치
            i = li[t]%2 # 1번 나무에 위치하는데 t시간에 1번에 떨어진다면 추가
        else : #이동횟수가 홀수 : 2번 나무에 위치
            i = li[t]//2 # 2번 나무에 위치하는데 t시간에 2번에 떨어진다면 추가
        dp[t][w] = max(dp[t-1][0:w+1])+i
print(max(dp[T]))
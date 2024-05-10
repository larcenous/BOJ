T = int(input())
for _ in range(T) :
    n = int(input())
    li = [list(map(int,input().split())) for __ in range(2)]
    dp = [[0]*n for __ in range(2)] # 각 요소를 선택했을 때의 최댓값을 저장
    dp[0][0] = li[0][0]
    dp[1][0] = li[1][0] #인접한 스티커는 선택할 수 없음
    if n == 1 :
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] = li[1][0] + li[0][1]
    dp[1][1] = li[0][0] + li[1][1]
    if n == 2 :
        print(max(dp[0][1], dp[1][1]))
        continue
    for i in range(2,n) :
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + li[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + li[1][i]
    print(max(dp[0][-1], dp[1][-1]))
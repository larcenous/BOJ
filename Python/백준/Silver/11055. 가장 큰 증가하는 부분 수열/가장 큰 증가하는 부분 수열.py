N = int(input())
A = list(map(int,input().split()))
dp = [0]*N
dp[0] = A[0]
for i in range(1,N) :
    for j in range(i) : 
        if A[j] < A[i] : #증가하는 부분 수열을 찾아야 하므로 i보다 앞에 존재하는 j index에 대해 비교
            dp[i] = max(dp[i], dp[j] + A[i]) #dp에 합을 저장
        else :
            dp[i] = max(dp[i],A[i]) #dp에 새로운 부분수열의 시작으로 갱신할지, 이전의 값을 유지할지 결정

print(max(dp))
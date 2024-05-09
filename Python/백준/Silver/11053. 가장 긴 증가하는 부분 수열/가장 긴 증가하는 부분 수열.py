N = int(input())
A = [0]
A.extend(list(map(int, input().split())))
DP = [0]*(N+1)

for i in range(1,N+1) :
    for j in range(i) : 
        if A[i] > A[j] :
            DP[i] = max(DP[i],DP[j]+1)

print(max(DP))
N = int(input())
TP = [list(map(int,input().split())) for _ in range(N)]
DP = [0]*(N+1)
for i in range(N) :
    for j in range(i+TP[i][0],N+1):
        if DP[j] < DP[i] + TP[i][1] :
            DP[j] = DP[i] + TP[i][1]
print(DP[-1])
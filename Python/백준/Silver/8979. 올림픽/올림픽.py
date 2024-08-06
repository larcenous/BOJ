N, K = map(int, input().split())

medals = [list(map(int, input().split())) for _ in range(N)]
    
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

idx = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if medals[idx][1:] == medals[i][1:]: 
        #같은 것이 있다면, 정렬되어 나타나는 첫번째 i에 1을 더한 것이 등수가 됨
        print(i+1)
        break
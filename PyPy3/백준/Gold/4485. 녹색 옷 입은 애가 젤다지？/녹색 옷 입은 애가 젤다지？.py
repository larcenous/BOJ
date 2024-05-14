import sys
from heapq import * 
inf = sys.maxsize

def Dijkstra(N,graph) :
    D = [[inf]*(N) for _ in range(N)]
    q = []
    dx,dy=[-1,0,1,0],[0,-1,0,1]
    heappush(q,(graph[0][0],0,0))
    D[0][0] = graph[0][0]
    while q :
        cost, x, y = heappop(q)
        if D[y][x] < cost : #유효한 탐색인지 확인
            continue
        for ddx,ddy in zip(dx,dy) :
            nx,ny = x+ddx, y+ddy
            if 0<=nx<=N-1 and 0<=ny<=N-1 :
                if cost + graph[ny][nx] < D[ny][nx] :
                    D[ny][nx] = cost + graph[ny][nx]
                    heappush(q,(D[ny][nx],nx,ny))
    return D[-1][-1]

i = 1
while True :
    N = int(input())
    if N == 0 :
        break
    graph = [list(map(int,input().split())) for _ in range(N)]
    print(f'Problem {i}: {Dijkstra(N,graph)}')
    i += 1
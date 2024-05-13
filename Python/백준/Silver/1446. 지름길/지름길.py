import sys
from heapq import *
inf = sys.maxsize

N, D = map(int,input().split())
graph = [[] for _ in range(D+1)]
for i in range(D) :
    graph[i].append((1,i+1))
for _ in range(N) :
    start, end, cost = map(int,input().split())
    if end > D :
        continue
    if end-start >= cost :
        graph[start].append((cost,end))

dist = [inf] *(D+1)
dist[0] = 0

def Dijkstra(start) :
    q = []
    heappush(q, (0,start))
    while q :
        cost, current = heappop(q)
        if cost > dist[current] : #일종의 visited와 같이 1차 필터링하여 의미없는 탐색을 제거
            continue
        for next_cost, next in graph[current] :        
            if dist[next] > dist[current] + next_cost :
                dist[next] = dist[current] + next_cost
                heappush(q, (dist[next] , next)) #왜 업데이트 한 cost를 heap에 넣어주는가?

Dijkstra(0)
print(dist[-1])
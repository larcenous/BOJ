import sys
from heapq import *
inf = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M) : #도시 간 거리 정보를 담은 그래프 초기화, heap을 이용할 것이므로 2차원 리스트로 구현하지 않음
    start, end, cost = map(int,input().split())
    graph[start].append((cost,end)) #cost를 앞에 두어 heappush, heappop 간에 cost를 기준으로 수행하게 됨

start, end = map(int,input().split()) #출발 도시와 도착 도시

visited = [False]*(N+1) #방문 여부 확인 리스트

D = [inf] * (N+1) #출발 도시로부터의 거리 정보를 저장할 리스트를 초기화
D[start] = 0 #출발 도시의 거리는 0으로 초기화

def Dijkstra(start) :
    min_heap = []
    heappush(min_heap,(0,start))
    while min_heap :
        cost, current = heappop(min_heap)
        if visited[current] :
            continue
        visited[current] = True
        for cost, next in graph[current] :
            if not visited[next] :
                if D[current] + cost < D[next] :
                    D[next] = D[current] + cost
                    heappush(min_heap, (D[next], next))

Dijkstra(start)
print(D[end])
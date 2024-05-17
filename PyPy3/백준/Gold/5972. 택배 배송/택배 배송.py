import sys
from heapq import *
inf = sys.maxsize

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    A,B,C = map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

D = [inf]*(N+1)
D[1] = 0

def Dijkstra() :
    hq = [(0,1)]
    while hq :
        cost, current = heappop(hq)
        if D[current] < cost :
            continue
        for next_cost, next_node in graph[current] :
            if D[current] + next_cost < D[next_node] :
                D[next_node] = D[current] + next_cost
                heappush(hq,(D[next_node], next_node))

Dijkstra()
print(D[-1])
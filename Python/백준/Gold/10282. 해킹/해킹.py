import sys
from heapq import *
inf = sys.maxsize
input = sys.stdin.readline

def Dijkstra(n, start) :
    D = [inf]*(n+1)
    D[start] = 0
    hq = [(0,start)]
    while hq :
        current_cost, current_node = heappop(hq)
        if D[current_node] < current_cost :
            continue
        for next_cost, next_node in graph[current_node] :
            if D[next_node] > D[current_node] + next_cost :
                D[next_node] = D[current_node] + next_cost
                heappush(hq,(D[next_node],next_node))
    D.sort()
    '''for i in range(len(D)-1,-1,-1) :
        if D[i] != inf :
            return i+1,D[i]'''
    cnt = sum(1 for d in D if d != inf)
    maximum = max(d for d in D if d != inf)
    return cnt,maximum

T = int(input())
for _ in range(T) :
    n,d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for __ in range(d) :
        a,b,s=map(int,input().split())
        graph[b].append((s,a))

    print(*Dijkstra(n,c))
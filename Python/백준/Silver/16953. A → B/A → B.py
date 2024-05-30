from collections import deque
import sys
inf = sys.maxsize
A, B = map(int,input().split())

def BFS(A,B) :
    ans = inf
    deq = deque([(A,1)])
    while deq :
        current, cnt = deq.popleft()
        num1 = current * 2
        num2 = current*10 + 1
        if num1 == B or num2 == B:
            ans = min(ans,cnt+1)
        if num1 < B :
            deq.append((num1,cnt+1))
        if num2 < B :
            deq.append((num2,cnt+1))
    if ans == inf :
        ans = -1
    return ans

ans = BFS(A,B)
print(ans)
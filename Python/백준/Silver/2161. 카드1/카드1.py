from collections import deque

N = int(input())
q = deque([])
ans = []
for i in range(1, N+1):
    q.append(i)

while (len(q) != 0):
    ans.append(q.popleft())
    if(len(q) != 0):
        q.append(q.popleft())

for j in ans:
    print(j, end =" ")
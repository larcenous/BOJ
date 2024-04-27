u,d = [0]*4,[0]*4
for i in range(4) :
    d[i], u[i] = map(int,input().split())
now = 0
maximum = 0
for U,D in zip(u,d) :
    now -= D
    now += U
    maximum = max(now,maximum)
print(maximum)
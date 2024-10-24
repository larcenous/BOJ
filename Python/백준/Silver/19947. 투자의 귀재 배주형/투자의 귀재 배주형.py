import math

n, y = map(int,input().split())
li = [0]*(y+1)
li[0]=n
if y >= 1 :
    for i in range(1,y+1) :
        li[i] = max(math.trunc(li[i-1]*1.05),li[i])
        if y >= 5 :
            li[i] = max(math.trunc(li[i-5]*1.35),li[i])
        if y >= 3 :
            li[i] = max(math.trunc(li[i-3]*1.2),li[i])

print(li[y])        
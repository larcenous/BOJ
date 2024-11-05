import math
li = list(map(int,input().split()))
N, KWF = map(int,input().split())
ans = 0
for i in range(len(li)//2) :
    ans += li[2*i]*li[2*i+1]
ans = math.trunc(math.trunc(ans/5)* N / KWF)
print(ans)
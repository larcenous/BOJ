import math
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
A = [a-B for a in A]
res = N
for a in A :
    if a > 0 :
        res += math.ceil(a / C)
print(res)
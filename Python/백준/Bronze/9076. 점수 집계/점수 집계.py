T = int(input())
for _ in range(T) :
    li = list(map(int,input().split()))
    li = sorted(li)
    li = li[1:4]
    if li[-1] - li[0] >= 4 :
        print('KIN')
    else :
        print(sum(li))
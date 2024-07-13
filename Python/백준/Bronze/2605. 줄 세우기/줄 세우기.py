n = int(input())
li = list(map(int,input().split()))
li2= []
for i in range(n) :
    if li[i] == 0 :
        li2.insert(0,i+1)
    else :
        li2.insert(li[i],i+1)

for i in reversed(li2):
    print(i,end=' ')
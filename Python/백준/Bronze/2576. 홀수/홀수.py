li = []
for _ in range(7) :
    tmp = int(input())
    if tmp%2 != 0 :
        li.append(tmp)
if len(li) > 0 :
    print(sum(li))
    print(min(li))
else :
    print(-1)
N = int(input())
li = [input().rstrip() for _ in range(N)]
a, b = 0,0
for i in li :
    tmp = i.split('X')
    for point in tmp :
        if '..' in point :
            a += 1

newli = []
for i in range(N) :
    tmp = ''
    for j in range(N) :
        tmp += li[j][i]
    newli.append(tmp)

for i in newli :
    tmp = i.split('X')
    for point in tmp :
        if '..' in point :
            b += 1

print(a,b)
N = int(input())
K = input()
a = 0
b = 0
for i in K :
    if int(i)%2 == 0 :
        a += 1
    else :
        b += 1

if a > b :
    print(0)
elif a < b :
    print(1)
else :
    print(-1)
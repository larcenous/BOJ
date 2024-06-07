N = int(input())
li = [int(input()) for i in range(N)]
if sum(li) > len(li)-sum(li) :
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')
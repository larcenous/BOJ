i = 1
while True :
    L, P, V = map(int,input().split())
    if L == 0 and P==0 and V==0 :
        break
    if V%P>L : 
        print(f'Case {i}: {V//P*L+L}')
    else :
        print(f'Case {i}: {V//P*L+V%P}')
    i += 1
a,b,c,d,e = map(int,input().split())
ans = 4*e-a-b-c-d
if ans < 0 :
    print(0)
else :
    print(ans)
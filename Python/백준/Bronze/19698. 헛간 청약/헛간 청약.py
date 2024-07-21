N,W,H,L = map(int,input().split())
a = W//L
b = H//L
ans = a*b
if ans > N :
    ans = N
print(ans)
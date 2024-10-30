n,k,t = map(int,input().split())

d = list(map(int,input().split()))
ans = 0
for i in range(n) :
    if t > k :
        t += d[i]-abs(t-k)
    elif t < k :
        t += d[i]+abs(t-k)
    else :
        t += d[i]
    ans += abs(t-k)
print(ans)
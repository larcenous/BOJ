n = int(input())
p, q, r, s = map(int, input().split())
a = int(input())

ans = [0]*(n+1)
for i in range(1,n+1):
    if i == 1:
        ans[i] = a
        continue
    if i%2 == 0:
        ans[i]=(p*ans[(i//2)])+q
    else:
        ans[i]=(r*ans[(i//2)])+s
print(sum(ans))
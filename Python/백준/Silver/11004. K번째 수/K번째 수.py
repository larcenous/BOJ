N, K = map(int,input().split())
ans = list(map(int,input().split()))
ans = sorted(ans)
print(ans[K-1])
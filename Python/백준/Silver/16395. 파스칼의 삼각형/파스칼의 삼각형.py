n,k = map(int,input().split())
max_n = max(n-1,k-1)
memo = {}
memo[0] = 1
memo[1] = 1

def factorial(n) :
    if n in memo :
        return memo[n]
    else :
        memo[n] = factorial(n-1)*n
        return memo[n]

factorial(max_n)
ans = memo[n-1]//(memo[n-1-(k-1)]*memo[k-1])
print(ans)
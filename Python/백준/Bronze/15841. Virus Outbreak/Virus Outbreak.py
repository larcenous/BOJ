memo = {}
memo[1] = 1
memo[2] = 1
def fibo(n) :
    if n in memo :
        return memo[n]
    else :
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
while True :
    k = int(input())
    if k == -1 :
        break
    print(f'Hour {k}: {fibo(k)} cow(s) affected')    
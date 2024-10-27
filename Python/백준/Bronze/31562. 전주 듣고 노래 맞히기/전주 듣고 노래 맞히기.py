N, M = map(int,input().split())
memo = dict()
for _ in range(N) :
    T, S, *i = input().split()
    key = ''.join(i[:3]) 
    if not key in memo :
        memo[key] = S
    else :
        memo[key] = '?'
for _ in range(M) :
    key = ''.join(input().split())
    if not key in memo :
        print('!')
    else :
        print(memo[key])
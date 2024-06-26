N, L = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
for fruit in li :
    if fruit <= L :
        L += 1
print(L)
na, nb = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
C = sorted(list(A-B))
if len(C) == 0 :
    print(0)
else :
    print(len(C))
    print(*C)
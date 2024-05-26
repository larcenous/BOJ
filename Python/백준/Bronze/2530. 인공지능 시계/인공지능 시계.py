A,B,C=map(int,input().split())
D = int(input())
C += D
if C//60 > 0 :
    B += C//60
    C = C%60
if B//60 > 0 :
    A += B//60
    B = B%60
if A//24 > 0 :
    A = A%24

print(A,B,C)
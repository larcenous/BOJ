N = int(input())
A,B = map(int,input().split())
A = A//2
a = A+B
print(min(a,N))
A,B = input().split()
ans = ''
max_len = max(len(A),len(B))
while len(A) != len(B) :
    if len(A) < len(B) :
        A = '0' + A
    elif len(A) > len(B) :
        B = '0' + B
for i in range(max_len) :
    ans += str(int(A[i])+int(B[i]))
print(ans)
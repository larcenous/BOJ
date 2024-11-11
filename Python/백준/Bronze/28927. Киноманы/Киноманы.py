A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans_A = A[0]*3+A[1]*20+A[2]*120
ans_B = B[0]*3+B[1]*20+B[2]*120
if ans_A > ans_B :
    print('Max')
elif ans_A < ans_B :
    print('Mel')
else :
    print('Draw')
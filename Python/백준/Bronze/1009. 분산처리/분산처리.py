'''
0 10
1 1
2 2 4 8 6
3 9 7 1
4 4 6
5 5
6 6
7 9 3 1
8 8 4 2 6
9 9 1
'''
T = int(input())
for _ in range(T) :
    a, b = map(int,input().split())
    a = a%10

    if a == 0 : # 개수에 따라 경우의 수를 세분화
        print(10)
    elif a == 1 | a == 5 | a == 6:
        print(a)
    elif a == 4 | a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10 % 10 % 10)
        else :
            print((a**b) % 10 % 10 % 10)
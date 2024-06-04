N = int(input())
for _ in range(N) :
    string = list(input().rstrip())
    if ord(string[0]) >= 97 :
        string[0] = chr(ord(string[0])-32)
    print(''.join(string))
while True :
    string = input().rstrip()
    if string == 'END' :
        break
    print(string[::-1])
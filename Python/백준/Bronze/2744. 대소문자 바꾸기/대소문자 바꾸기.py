string = input()
for i in range(len(string)):
    tmp = ord(string[i])
    if tmp >= 97 :
        print(chr(tmp-32), end='')
    else :
        print(chr(tmp+32), end='')
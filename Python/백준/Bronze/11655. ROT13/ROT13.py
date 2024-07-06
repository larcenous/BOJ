S = list(input().rstrip())
ans = []
for i in S :
    tmp = ord(i)
    if tmp == 32 : #' '
        ans.append(chr(tmp))
        continue
    if 122>=ord(i) & ord(i)>=97 : #소문자
        tmp = ord(i)+13
        if tmp > 122 :
            tmp -= 26
        ans.append(chr(tmp))
        continue
    elif 90>=ord(i) & ord(i)>=65 : #대문자
        tmp = ord(i)+13
        if tmp > 90 :
            tmp -= 26
        ans.append(chr(tmp))
        continue
    ans.append(i)
print(''.join(ans))
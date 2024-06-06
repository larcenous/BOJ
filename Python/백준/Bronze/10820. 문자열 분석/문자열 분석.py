while True:
    try:
        ans = [0] * 4
        temp = input()
        for i in range(len(temp)):
            num = ord(temp[i])
            if num >= 97 :
                ans[0] += 1
            elif num >= 65 :
                ans[1] += 1
            elif num >= 48 :
                ans[2] += 1
            elif num == 32:
                ans[3] += 1
        print(' '.join(map(str, ans)))
    except:
        break
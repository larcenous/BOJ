while True:
    try:
        ans = [0] * 4
        temp = input()
        for i in range(len(temp)):
            if temp[i].islower():
                ans[0] += 1
            elif temp[i].isupper():
                ans[1] += 1
            elif temp[i].isnumeric():
                ans[2] += 1
            elif temp[i].isspace():
                ans[3] += 1
        print(' '.join(map(str, ans)))
    except:
        break
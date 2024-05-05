dic = {'A' : 4.0, 'B' : 3.0, 'C' : 2.0, 'D' : 1.0, 'F' : 0.0}

grade = input()
ans = 0.0
if len(grade) == 1 :
    print(0.0)
else :
    ans += dic[grade[0]]
    if grade[1] == '+' :
        ans += 0.3
    elif grade[1] == '-' : 
        ans -= 0.3
    else :
        pass
    print(ans)
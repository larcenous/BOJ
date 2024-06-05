N = input()

if "0" not in N:
    print(-1)

else:
    tmp = 0
    for i in range(len(N)):
        tmp += int(N[i])
    if tmp % 3 != 0:
        print(-1)
    else:
        sorted_num = sorted(N, reverse=True)
        answer = ''.join(sorted_num)
        print(answer)
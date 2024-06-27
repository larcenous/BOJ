n = int(input())
i = 0
cnt = 0
while True:
    if n > i:
        i += 1
        n -= i
        cnt += 1
    else:
        break
print(cnt)
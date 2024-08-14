while True :
    N = int(input())
    if N == 0 :
        break
    li = [input() for _ in range(N)]
    li.sort(key=str.lower)
    print(li[0])
Dusa = int(input())

while True:
    try:
        Yobis = int(input())
        if Yobis >= Dusa:
            break
        Dusa += Yobis
    except EOFError:
        break
print(Dusa)
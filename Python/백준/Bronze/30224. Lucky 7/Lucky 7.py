n = input()
key1 = ('7' in n)
key2 = (int(n)%7 == 0)

if not key1 and not key2 :
    print(0)
elif not key1 and key2 :
    print(1)
elif key1 and not key2 :
    print(2) 
elif key1 and key2 :
    print(3)
    
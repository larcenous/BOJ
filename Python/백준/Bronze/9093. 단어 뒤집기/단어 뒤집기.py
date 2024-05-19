T = int(input())
for _ in range(T) :
    sentence = input().split()
    ans = []
    for word in sentence :
        ans.append(word[::-1])
    print(' '.join(ans))
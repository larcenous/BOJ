J, N = map(int,input().split())
li = []
for _ in range(N) :
    name = list(input().strip())
    score = 0
    for x in name :
        if x.isupper():
            score += 4
        elif x.islower() or x.isdigit() :
            score += 2
        elif x == ' ':
            score += 1
    li.append(score)

ans = 0
for i in li :
    if i <= J :
        ans += 1

print(ans)
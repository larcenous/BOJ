cnt = [0]*26
for s in input() :
    cnt[ord(s)-97] += 1
print(*cnt)
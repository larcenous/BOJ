K = int(input())
li = [0]*(K+1)
li[1] = 1
for i in range(2,K+1) :
    li[i] = li[i-1] + li[i-2]

print(li[K-1],li[K])
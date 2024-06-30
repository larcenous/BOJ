n = int(input())
milk_li = list(map(int, input().split()))
count = 0

for i in range(n):
   if milk_li[i] == count % 3:
        count += 1

print(count)
A = sorted([int(input().rstrip()) for _ in range(10)],reverse=True)
B = sorted([int(input().rstrip()) for _ in range(10)],reverse=True)
print(sum(A[:3]), sum(B[:3]))
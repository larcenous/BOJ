N, M = map(int, input().split())
ans = N
while N//M != 0:
    N //= M
    ans += N
print(ans)
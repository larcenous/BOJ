def hanoi_cal(n):
    if n == 1:
        return 1
    return 2 * hanoi_cal(n - 1) + 1

hanoi = [0] * 13
hanoi[1] = 1
for i in range(2, 13):
    hanoi[i] = hanoi_cal(i)

dp = [0] * 13
dp[1] = 1

print(dp[1])

# DP를 이용하여 최소 이동 횟수 계산
for i in range(2, 13):
    min_value = float('inf')
    for j in range(1, i + 1):
        if min_value > hanoi[j] + 2 * dp[i - j]:
            min_value = hanoi[j] + 2 * dp[i - j]
    dp[i] = min_value
    print(min_value)

def max_profit(schedule):
    n = len(schedule)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        if i == n-1:
            dp[i] = schedule[i][1]
            continue
        if i + schedule[i][0] <= n:
            dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])
        else:
            dp[i] = dp[i + 1]

    return dp[0]


# 입력 처리
N = int(input())
schedule = []
for _ in range(N):
    days, profit = map(int, input().split())
    schedule.append((days, profit))

# 최대 수익 계산 및 출력
result = max_profit(schedule)
print(result)

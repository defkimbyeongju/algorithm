def backtracking(s1, s2, res, n):
    global min_v
    if n == N:
        res += abs(home_x - s1) + abs(home_y - s2)
        min_v = min(min_v, res)
        return
    if res >= min_v:  # 가지 치기
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            temp = abs(s1 - customers[i][0]) + abs(s2 - customers[i][1])
            backtracking(customers[i][0], customers[i][1], res+temp, n + 1)
            used[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_v = 21e9
    start_x, start_y, home_x, home_y = arr[0], arr[1], arr[2], arr[3]
    used = [0] * N
    customers = [arr[i:i+2] for i in range(4, len(arr), 2)]
    backtracking(start_x, start_y, 0, 0)
    print(f'#{tc} {min_v}')
def backtracking(level, acc_height):
    global ans
    # 현재까지 탑이 선반 높이를 넘어간다면 앞으로는 더 볼 필요 없음
    if acc_height >= B:
        ans = min(ans, acc_height)
        return
    # 기저 조건
    if level == N:
        return
    # 해당 점원을 탑에 쓸 경우, 안 쓸 경우를 나눔
    backtracking(level+1, acc_height+arr[level])

    backtracking(level+1, acc_height)

T = int(input())
for tc in range(1,T+1):
    N,B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    backtracking(0, 0)
    print(f'#{tc} {ans-B}')
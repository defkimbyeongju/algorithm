def backtracking(cnt, total):
    global min_v
    if cnt == N:
        if total < min_v:
            min_v = total
        return
    if total > min_v:
        return
    for i in numbers:
        if i in path:
            continue
        path[cnt] = i
        backtracking(cnt+1, total+costs[i-1][cnt])
        path[cnt] = 0


T = int(input())
for tc in range(1,T+1):
    min_v = 21e8
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    numbers = [i for i in range(1,N+1)] # 각 공장이 다른 제품을 담당하게 하기 위해
    path = [0]*N
    backtracking(0,0)
    print(f'#{tc} {min_v}')

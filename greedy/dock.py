T = int(input())
for tc in range(1,T+1):
    N = int(input())
    dock = [list(map(int, input().split())) for _ in range(N)]
    dock.sort(key=lambda x:x[1])
    total = 1
    end = dock[0][1]
    for i in range(1,N):
        if dock[i][0] >= end:
            total += 1
            end = dock[i][1]
    print(f'#{tc} {total}')
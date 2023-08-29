T = int(input())
for tc in range(1,T+1):
    N = int(input())
    apple = [list(map(int, input().split())) for _ in range(N)]
    max_value = max(sum(apple, []))
    apple_loc = []
    dir = ['right', 'low', 'left', 'high']
    rotation = 1
    for i in range(1, max_value+1):
        for j in range(N):
            for k in range(N):
                if apple[j][k] == i:
                    apple_loc.append((j,k))
    for i in range(1, max_value):
        if dir[rotation%4] == 'low':
            if apple_loc[i-1][1] == apple_loc[i][1] and apple_loc[i-1][0] < apple_loc[i][0]:
                continue
            elif apple_loc[i-1][1] > apple_loc[i][1] and apple_loc[i-1][0] <= apple_loc[i][0]:
                rotation += 1
            elif apple_loc[i-1][1] > apple_loc[i][1] and apple_loc[i-1][0] > apple_loc[i][0]:
                rotation += 2
            else:
                rotation += 3
        elif dir[rotation%4] == 'left':
            if apple_loc[i-1][0] > apple_loc[i][0] and apple_loc[i-1][1] >= apple_loc[i][1]:
                rotation += 1
            elif apple_loc[i-1][1] > apple_loc[i][1] and apple_loc[i-1][0] == apple_loc[i][0]:
                continue
            elif apple_loc[i-1][1] < apple_loc[i][1] and apple_loc[i-1][0] > apple_loc[i][0]:
                rotation += 2
            else:
                rotation += 3
        elif dir[rotation%4] == 'high':
            if apple_loc[i-1][1] < apple_loc[i][1] and apple_loc[i-1][0] >= apple_loc[i][0]:
                rotation += 1
            elif apple_loc[i-1][1] == apple_loc[i][1] and apple_loc[i-1][0] > apple_loc[i][0]:
                continue
            elif apple_loc[i-1][1] < apple_loc[i][1] and apple_loc[i-1][0] < apple_loc[i][0]:
                rotation += 2
            else:
                rotation += 3

        elif dir[rotation%4] == 'right':
            if apple_loc[i-1][0] < apple_loc[i][0] and apple_loc[i-1][1] <= apple_loc[i][1]:
                rotation += 1
            elif apple_loc[i-1][1] < apple_loc[i][1] and apple_loc[i-1][0] == apple_loc[i][0]:
                continue
            elif apple_loc[i-1][1] > apple_loc[i][1] and apple_loc[i-1][0] < apple_loc[i][0]:
                rotation += 2
            else:
                rotation += 3
    print(f'#{tc} {rotation}')

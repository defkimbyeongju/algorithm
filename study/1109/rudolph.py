def move(y,x,dy,dx,value):
    santa = arr[y][x]
    ny = y + dy
    nx = x + dx
    if 0<=ny<N and 0<=nx<N: # 밀려나도 범위 안에 있다면
        if arr[ny][nx] != 0: # 그 자리에도 누군가 있다면
            move(ny,nx,dy,dx, santa)
        arr[y][x] = value
    else: # 바깥으로 밀려나면 out 처리
        santa_loc[santa-1][3] = -1



N, M, P, C, D = map(int, input().split())
arr = [[0]*N for _ in range(N)]
Ry, Rx = map(int,input().split())
Ry -= 1
Rx -= 1
arr[Ry][Rx] = -1 # 루돌프는 -1로 표시
santa_loc = [[] for _ in range(P)] # 산타들의 좌표, 점수, 기절여부를 체크할 리스트
for _ in range(P):
    santa, Sy, Sx = map(int, input().split())
    santa_loc[santa-1] = [Sy-1, Sx-1, 0, 0] # y좌표, x좌표, 점수, 기절 여부(기절하면 1, 아웃이면 -1)
    arr[Sy-1][Sx-1] = santa # 산타들은 각자의 번호로 표시
print(arr)
for _ in range(M):
    # 루돌프 먼저 이동
    arr[Ry][Rx] = 0
    distance = [[] for _ in range(P)]
    for i in range(P):
        if santa_loc[i][3] == -1: # 아웃인 곳은 제껴야됨
            distance[i] = [10000,santa_loc[i][0],santa_loc[i][1], i]
            continue
        temp = (Ry - santa_loc[i][0]) ** 2 + (Rx - santa_loc[i][1]) ** 2
        distance[i] = [temp, santa_loc[i][0],santa_loc[i][1], i] # 거리, y좌표, x좌표, 인덱스
    distance.sort(key=lambda x:(x[0], -x[1], -x[2]))
    # 좌표 차이로 다음 방향 정해주기
    if Ry == distance[0][1]:
        dy = 0
    elif Ry > distance[0][1]:
        dy = -1
    else:
        dy = 1
    if Rx == distance[0][2]:
        dx = 0
    elif Rx > distance[0][2]:
        dx = -1
    else:
        dx = 1
    # 방향 이동
    Ry += dy
    Rx += dx
    # 루돌프가 이동해서 산타 만나면 산타 튕겨져 나가기
    if Ry == distance[0][1] and Rx == distance[0][2]:
        imsi = arr[Ry][Rx] # 루돌프랑 충돌한 산타 번호
        arr[Ry][Rx] = -1
        dy *= C
        dx *= C
        # y = santa_loc[distance[0][3]][0]
        # x = santa_loc[distance[0][3]][1]
        ny = Ry+dy
        nx = Rx+dx
        point = santa_loc[distance[0][3]][2]
        point += C
        # 아웃 처리
        if ny >= N or ny < 0 or nx >= N or nx < 0: # 범위 밖이라면
            santa_loc[distance[0][3]] = [ny, nx, point, -1]
        else:
        # 기절 처리
            santa_loc[distance[0][3]] = [ny, nx, point, 1]
        # 이동한 위치에 다른 산타가 있을 경우 상호작용
            if arr[ny][nx] != 0:
                move(ny,nx,dy//C,dx//C,imsi)
            else:
                arr[ny][nx] = imsi
    else:
        arr[Ry][Rx] = -1

    # 산타 이동 차례
    for i in range(P):
        if santa_loc[i][3] == -1: # 기절이나 아웃이면 움직이지 않음
            continue
        elif santa_loc[i][3] == 1:
            santa_loc[i][3] -= 1
            continue
        y,x = santa_loc[i][0], santa_loc[i][1]
        dist = (Ry-y) ** 2 + (Rx-x) ** 2
        # 상,우,하,좌 순서
        for dy,dx in [(-1,0), (0,1), (1,0), (0,-1)]:
            ny,nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N: # 범위 안에 들어오고
                if (ny-y) ** 2 + (nx-x) ** 2 < dist: # 거리가 더 가까워지며
                    if arr[ny][nx] == 0: # 해당 칸이 비어있으면
                        arr[y][x] = 0
                        arr[ny][nx] = i+1
                        break # 움직였으면 끝!
                    elif arr[ny][nx] == -1: # 루돌프랑 충돌한다면
                        arr[y][x] = 0 # 산타 위치 초기화
                        santa_loc[i][2] += D
                        dy *= -1
                        dx *= -1
                        ny += dy*D
                        nx += dx*D
                        if 0<=ny<N and 0<=nx<N: # 범위 안에 들어올 때
                            if arr[ny][nx] != 0:
                                move(ny,nx,dy,dx,i+1)
                            else:
                                arr[ny][nx] = i+1
                        else: # 나가리 되면
                            santa_loc[i] = [ny, nx, santa_loc[i][2], -1]
    print(arr)
for i in range(P):
    print(santa_loc[i][2], end=' ')

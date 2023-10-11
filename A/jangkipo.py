from collections import deque
sero_dir = [(1,0),(-1,0)]
garo_dir = [(0,1),(0,-1)]
def janki(i, j): # i: y좌표, j: x좌표
    queue = deque()
    queue.append([i,j,0])
    while queue:
        now_y,now_x,depth = queue.popleft()
        for y,x in sero_dir: # 수직 이동
            ny, nx = now_y+y, now_x+x
            if 0>ny or ny>=N: # 범위 벗어나면 탐색 x
                continue
            if y == 1: # 아래로 갑니다
                while True:
                    if arr[ny][nx] == 1: # 쫄을 만난다면
                        if ny != N-1: # 마지막 값이 아니라면
                            recent = ny # 가장 최신에 나온 쫄
                            for k in range(ny+1, N): # 다음 값부터 탐색
                                if arr[k][nx] == 0: # 빈 땅이면 그냥 queue에 추가
                                    if depth+1 < 3: # 3보다 작아야 됨
                                        queue.append([k,nx,depth+1])
                                elif arr[k][nx] == 1: # 다음에 쫄이 온다면
                                    if depth+1 < 3: # 3보다 작으면 다음 이동 가능
                                        queue.append([k,nx,depth+1])
                                    if [k,nx] not in jjol: # 중복되지 않는다면 추가. 3까지도 가능
                                        jjol.append([k,nx])
                                    if k == recent+1: # 붙어 있다면 여기서 끝내자
                                        break
                                    recent = k # 최신 쫄 갱신
                        break # 어차피 쫄 만나면 끝내야 됨
                    ny += 1
                    if ny >= N: # ny가 범위 벗어나면 바로 종료
                        break
            elif y == -1: # 위로 갑니다
                while True:
                    if arr[ny][nx] == 1: # 쫄을 만난다면
                        if ny != 0: # 처음 값이 아니라면
                            recent = ny # 가장 최신에 나온 쫄
                            for k in range(ny-1, -1, -1): # 다음 값부터 탐색
                                if arr[k][nx] == 0: # 빈 땅이면 그냥 queue에 추가
                                    if depth+1 < 3: # 3보다 작아야 됨
                                        queue.append([k,nx,depth+1])
                                elif arr[k][nx] == 1: # 다음에 쫄이 온다면
                                    if depth+1 < 3: # 3보다 작아야 됨
                                        queue.append([k,nx,depth+1])
                                    if [k,nx] not in jjol: # 중복되지 않는다면 추가
                                        jjol.append([k,nx])
                                    if k == recent-1: # 붙어 있다면 여기서 끝내자
                                        break
                                    recent = k # 최신 쫄 갱신
                        break # 어차피 쫄 만나면 끝내야 됨
                    ny -= 1
                    if ny < 0: # ny가 범위 벗어나면 바로 종료
                        break

        for y,x in garo_dir: # 수평 이동
            ny, nx = now_y+y, now_x+x
            if 0>nx or nx>=N: # 범위 벗어나면 탐색 x
                continue
            if x == 1: # 오른쪽으로 갑니다
                while True:
                    if arr[ny][nx] == 1: # 쫄을 만난다면
                        if nx != N-1: # 마지막 값이 아니라면
                            recent = nx # 가장 최신에 나온 쫄
                            for k in range(nx+1, N): # 다음 값부터 탐색
                                if arr[ny][k] == 0: # 빈 땅이면 그냥 queue에 추가
                                    if depth+1 < 3: # 3보다 작아야 됨
                                        queue.append([ny,k,depth+1])
                                elif arr[ny][k] == 1: # 다음에 쫄이 온다면
                                    if depth+1 < 3: # 3보다 작아야 됨
                                        queue.append([ny,k,depth+1])
                                    if [ny,k] not in jjol: # 중복되지 않는다면 추가
                                        jjol.append([ny,k])
                                    if k == recent+1: # 붙어 있다면 여기서 끝내자
                                        break
                                    recent = k # 최신 쫄 갱신
                        break # 어차피 쫄 만나면 끝내야 됨
                    nx += 1
                    if nx >= N: # ny가 범위 벗어나면 바로 종료
                        break
            elif x == -1: # 왼쪽으로 갑니다
                while True:
                    if arr[ny][nx] == 1: # 쫄을 만난다면
                        if nx != 0: # 처음 값이 아니라면
                            recent = nx # 가장 최신에 나온 쫄
                            for k in range(nx-1, -1, -1): # 다음 값부터 탐색
                                if arr[ny][k] == 0: # 빈 땅이면 그냥 queue에 추가
                                    if depth+1 < 3: # 3보다 작아야 됨
                                        queue.append([ny,k,depth+1])
                                elif arr[ny][k] == 1: # 다음에 쫄이 온다면
                                    if depth+1 < 3: # 3보다 작아야 됨
                                        queue.append([ny,k,depth+1])
                                    if [ny,k] not in jjol: # 중복되지 않는다면 추가
                                        jjol.append([ny,k])
                                    if k == recent-1: # 붙어 있다면 여기서 끝내자
                                        break
                                    recent = k # 최신 쫄 갱신
                        break # 어차피 쫄 만나면 끝내야 됨
                    nx -= 1
                    if nx < 0: # ny가 범위 벗어나면 바로 종료
                        break

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    jjol = []
    start_y, start_x = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_y, start_x = i, j
                break
    janki(start_y, start_x)
    print(f'#{tc} {len(jjol)}')
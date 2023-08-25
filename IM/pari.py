def spray(i, j):
    dir_1 = [(0,1),(1,0),(-1,0),(0,-1)]
    dir_2 = [(1,1),(-1,-1),(1,-1),(-1,1)]
    total_1 = pari_zone[i][j]
    total_2 = pari_zone[i][j]
    for x,y in dir_1:
        for power in range(1,M):
            ni, nj = i+(x*power), j+(y*power)
            if 0<=ni<N and 0<=nj<N:
                total_1 += pari_zone[ni][nj]
    for x,y in dir_2:
        for power in range(1,M):
            ni, nj = i+(x*power), j+(y*power)
            if 0<=ni<N and 0<=nj<N:
                total_2 += pari_zone[ni][nj]
    return max(total_1,total_2)



T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    pari_zone = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            result.append(spray(i,j))
    print(f'#{tc} {max(result)}')


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir = [(0,1),(0,-1), (1,0), (-1,0)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                stack = []
                for k,p in range(4):
                    ni, nj = i+k, j+p
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == 0:
                            stack.append((ni, nj))

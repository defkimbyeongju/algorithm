dir = [(0,1),(1,0),(0,-1),(-1,0)]
def recur(i,j,level,num):
    if level == 7:
        result.add(num)
        return
    for y,x in dir:
        ny, nx = i+y, j+x
        if 0 <=ny<4 and 0<=nx<4:
            recur(ny,nx,level+1, num+arr[ny][nx])

T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            recur(i,j,1,arr[i][j])
    print(f'#{tc} {len(result)}')
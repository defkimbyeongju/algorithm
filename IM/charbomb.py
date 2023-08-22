'''
T = int(input())
for tc in range(1,T+1):
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    N,M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            point = arr[i][j]
            for y,x in dir:
                for k in range(1,M+1):
                    ny,nx = i+(y*k), j+(x*k)
                    if 0<=ny<N and 0<=nx<N:
                        point += arr[ny][nx]

            if max_v < point:
                max_v = point

    print(f'#{tc} {max_v}')
'''

'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(i,N):
                for p in range(j,N):
                    if arr[i][j] == arr[k][p]:
                        square = (k-i+1) * (p-j+1)
                        if max_v < square:
                            max_v = square
                            val_cnt = 1
                        elif max_v == square:
                            val_cnt += 1

    print(f'#{tc} {val_cnt}')
'''
'''
def captcha(s, p):
    a = p.pop(0)
    for i in s:
        if i == a:
            if not p:
                return 1
            else:
                a = p.pop(0)
    return 0
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    sample = list(map(int,input().split()))
    pass_code = list(map(int, input().split()))
    result = captcha(sample, pass_code)
    print(f'#{tc} {result}')
'''

'''
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    answer = list(map(int, input().split()))
    student_answer = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    min_v = 200
    for i in range(N):
        score = 0
        cnt = 0
        for j in range(M):
            if answer[j] == student_answer[i][j]:
                cnt += 1
                score += cnt
            else:
                cnt = 0
        if max_v < score:
            max_v = score
        if min_v > score:
            min_v = score
    print(f'#{tc} {max_v-min_v}')
'''

'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                y, x = i, j
    max_v = 0
    for k in range(N+1):
        for p in range(N+1):
            if arr[k][p] == 1:
                tmp = (k-y)**2 + (p-x)**2
                if max_v < tmp:
                    max_v = tmp
    result = 1
    while result**2 < max_v:
        result += 1
    print(f'#{tc} {result}')
'''
'''
def dfs(v):
    visited[v] = 1
    for i in tree[v]:
        dfs(i)

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    visited = [0] * (E+2)
    for i in range(E):
        tree[arr[i*2]].append(arr[i*2+1])
    dfs(N)
    print(f'#{tc} {sum(visited)}')
'''



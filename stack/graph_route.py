# def dfs(S, G, V, adj_m):
#     result = 0
#     stack = []   # stack 생성
#     visited = [0] * (V+1)   # visited 생성
#     visited[S] = 1      # 시작점 방문 표시
#     while True:
#         for w in range(1, V+1):    # 현재 정점 S에 인접하고 미방문 w 찾기
#             if adj_m[S][w] == 1 and visited[w] == 0:
#                 stack.append(S) # push(v), v = w
#                 S = w
#                 visited[S] = 1  # w방문 visited
#                 break
#         else:
#             if stack:  # stack에 지나온 정점이 남아있으면
#                 S = stack.pop()  # pop()해서 다시 다른 w 찾을 S 준비
#             else:
#                 break  # while True 탐색 끝
#     if visited[G] == 1:
#         return 1
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     adj_m = [[0] * (V+1) for _ in range(V+1)]
#     visited = [0] * (V+1)
#     arr = [list(map(int, input().split())) for _ in range(E)]
#     for i in range(E):
#         v1, v2 = arr[i][0], arr[i][1]
#         adj_m[v1][v2] = 1
#     S, G = map(int, input().split())
#     print(f'#{tc} {dfs(S, G, V, adj_m)}')


# 강사님 풀이
# T = int(input())
#
# def dfs(start, end):
#     stack = []
#     visited = [False] * (v+1)
#     stack.append(start)
#     while stack:
#         now = stack.pop()
#         visited[now] = True
#         for next in range(1, v+1):
#             if node[now][next] and not visited[next]: # 방문하지 않았고, 연결되어 있다면 추가
#                 stack.append(next)
#     if visited[end]:
#         return 1
#     else:
#         return 0
#
# for tc in range(1,T+1):
#     v, e = map(int,input().split())
#     node = [[0 for _ in range(v+1)] for _ in range(v+1)]  # 인접행렬 초기화
#     for _ in range(e):
#         start, end = map(int, input().split())
#         node[start][end] = 1 # 해당 인접행렬에 1 할당 -> 연결됨
#     S,G = map(int, input().split())
#     print(f'#{tc} {dfs(S, G)}')
#


# def dfs(now):
#     print(now, end=' ')
#     for i in range(N):
#         # 현재 노드(now)와 i번째 노드가 연결되어 있다면
#         if adj_m[now][i] == 1:
#             # 재귀로 접근
#             dfs(i)
#
#
# N = int(input())
# adj_m = [list(map(int, input().split())) for _ in range(N)]
# dfs(0)

'''
5
0 1 1 0 0
0 0 0 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(now):
    stack = []
    stack.append(now)
    while stack:
        for i in range(N):
            if arr[now][i]:
                stack.append(i)
                for j in range(N):
                    if arr[i][j]:
                        stack.append(j)
                        print(*stack)
                        stack.pop()
                stack.pop()
        stack.pop()
dfs(0)

# 강사님 풀이

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*3

def dfs(now, level):
    global visited
    visited[level] = str(now)
    if level == 2:
        print(' '.join(visited))
    for i in range(N):
        if arr[now][i]:
            dfs(i, level+1)

dfs(0, 0)
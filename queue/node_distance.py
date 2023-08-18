
def bfs(S,G):
    visited = [0]*(V+1)
    queue = []
    queue.append(S)
    visited[S] = 1
    while queue:
        t = queue.pop(0)
        if t == G:
            return visited[t] - 1

        for w in adj_lst[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t]+1
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    adj_lst = [[] for _ in range(V+1)]
    for i in range(E):
        v1,v2 = arr[i][0], arr[i][1]
        adj_lst[v1].append(v2)
        adj_lst[v2].append(v1)
    S,G = map(int,input().split())
    result = bfs(S,G)
    print(f'#{tc} {result}')


# 강사님 풀이
# from collections import deque
# def bfs(start, end):
#     queue = deque([start, 0]) # 큐에 시작노드와, 초기거리 0을 넣기
#     while queue:
#         n, cnt = queue.popleft()
#
#         if not visited[n]: # 노드를 방문하지 않았다면
#             visited[n] = 1 # 방문 표시
#         for j in arr[n]: # 현재 노드에 연결된 노드를 탐색
#             if not visited[j] and j == end: # 목표 노드에 도착하면
#                 return cnt + 1  # 거리 +1 반환
#             elif not visited[j]: # 아직 방문하지 않은 노드
#                 queue.append([j, cnt +1]) # 인큐
#     return 0 # 경로가 없으면 0 반환
#
#
# T = int(input())
# for tc in range(1,T+1):
#     V,E = map(int,input().split())
#     arr = [[] for _ in range(V+1)] # 인접행렬 초기화
#     visited = [0]*(V+1)
#     for i in range(E):  # 간선 개수만큼 반복해서 인접 행렬 만들기
#         n1, n2 = map(int, input().split())
#         arr[n1].append(n2)
#         arr[n2].append(n1)
#     S, G = map(int, input().split())
#     result = bfs(S,G)
#     print(f'#{tc} {result}')

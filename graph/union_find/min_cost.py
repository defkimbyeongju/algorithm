# from collections import deque
#
# def bfs(r,c):
#     dir = [(1,0),(0,1),(-1,0),(0,-1)]
#     visited[r][c] = 0 # 시작지점 연료소비량 0 초기화
#     queue = deque()
#     queue.append((r,c))
#     while queue: # 큐에 노드가 있으면 계속 탐색
#         r, c = queue.popleft()
#         for dr, dc in dir:
#             nr, nc = r+dr, c+dc
#             # 이동 가능한 범위 내에 있을 때
#             if 0<=nr<N and 0<=nc<N:
#                 val = 0
#                 # 1. 현재 지점보다 높은 지역으로 이동할 때 높이 차이
#                 if arr[r][c] < arr[nr][nc]:
#                     val = arr[nr][nc] - arr[r][c]
#                 # 2. 이동하려는 위치의 연료 소비량 갱신
#                 if visited[r][c] + 1 + val < visited[nr][nc]:
#                     visited[nr][nc] = visited[r][c] + 1+ val
#                     queue.append((nr,nc))
#     return visited[N-1][N-1]
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[float('inf')]*N for _ in range(N)]
#     result = bfs(0,0)
#     print(f'#{tc} {result}')


# 다익스트라 버전

import heapq
# 1. 누적 거리를 계속 저장
# 2. 우선순위 큐
# 인접 리스트

def dijkstra():
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0,0,0))
    distance[0][0] = 0

    while pq:
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue
        # 인접 노드를 확인
        graph = []
        for y,x in dir:
            ny, nx =
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크네?
            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    INF = int(1e9)
    distance = [INF] * (n+1)
    dijkstra(0)
    print(f'#{tc} {distance[n]}')
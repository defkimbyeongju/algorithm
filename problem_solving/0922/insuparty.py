import heapq
def dikj(s,g):
    pq = []
    heapq.heappush(pq,(0,s))
    distance = [float('inf')]*N
    distance[s] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        for next in graph[now]:
            next_node = next[0]
            next_dist = next[1]
            # 다음 노드까지 이동할 때 드는 누적 비용
            new_cost = distance[now] + next_dist
            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, [new_cost, next_node])
    return distance



T = int(input())
for tc in range(1,T+1):
    N,M,X = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        f,t,w = map(int,input().split())
        graph[f-1].append([t-1,w])
    max_v = 0
    distance_from_x = dikj(X-1)
    for i in range(N):
        if i == X-1:
            continue
        temp = dikj(i)[X-1] + distance_from_x[i]
        max_v = max(max_v, temp)
    print(f'#{tc} {max_v}')
import heapq

def func(s):
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, [0,s])
    distance[s] = 0

    while pq:
        acc, now = heapq.heappop(pq)
        if distance[now] < acc:
            continue
        for nex in graph[now]:
            next_node, dist = nex[0], nex[1]
            if distance[next_node] <= distance[now] + dist:
                continue
            distance[next_node] = distance[now] + dist
            heapq.heappush(pq, [distance[next_node],next_node])


T = int(input())
for tc in range(1,T+1):
    n, e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        f,t,w = map(int, input().split())
        graph[f].append([t,w])
    distance = [float('inf')] * (n+1)
    func(0)
    print(f'#{tc} {distance[n]}')
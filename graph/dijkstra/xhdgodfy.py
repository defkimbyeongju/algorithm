import heapq
def dijkstra(s):
    distance = [float('inf')] * (N+1)
    distance[s] = 0
    pq = [(0,s)]
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next_node, weight in graph[now]:
            new_cost = dist + weight
            if new_cost >= distance[next_node]:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
    return distance[B]


N,M,K = map(int, input().split())
A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    f,t,w = map(int, input().split())
    graph[f].append([t,w])
    graph[t].append([f,w])
if K == 0:
    print(dijkstra(A))
else:
    years = [0]
    for _ in range(K):
        p = int(input())
        years.append(p)
    for i in range(K+1):
        for j in range(1,N+1):
            for k in range(len(graph[j])):
                graph[j][k][1] += years[i]
        print(dijkstra(A))
# 프림 알고리즘으로 MST 구현
import heapq
def prim(start):
    result = 0
    heap = []
    # MST에 포함되었는지 여부
    MST = [0] * V
    # (가중치, 정점) heappush
    heapq.heappush(heap, (0,start))
    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)
        # 갈 수 없는 노드라면 pass
        if MST[v]:
            continue
        # 방문 체크. 방문한 순간 누적합 추가
        MST[v] = 1
        result += weight
        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나, 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            # 갈 수 있으면 우선 순위 큐에 넣는다. 어차피 적은 가중치 값들이 먼저 나오기 때문에 더 높은 값들은 pop해서 사라짐
            heapq.heappush(heap, (graph[v][next], next))
    return result

V, E = map(int, input().split())
# 인접 행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w # 무방향 그래프이기 때문에
print(prim(0))


# 
# 모든 간선들 중 비용이 가장 적은 간선부터 고르자
V,E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f,t,w])
edge.sort(key=lambda x:x[2])

# 사이클 발생 여부를 union find로 해결
parents = [i for i in range(V)]
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

cnt = 0 # 현재 방문한 정점 수
ans = 0 # 합계
for f,t,w in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        ans += w
        union(f,t)
        # MST 구성이 끝나면
        if cnt == V:
            break
print(ans)
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    # 부모 찾기
    x = find_set(x)
    y = find_set(y)
    
    # 부모가 같으면 리턴
    if x == y:
        return
    # 더 작은 값을 부모로 설정
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    edge = []
    for _ in range(E):
        f,t,w = map(int, input().split())
        edge.append([f,t,w])
    edge.sort(key=lambda x: x[2])
    parents = [i for i in range(V+1)]
    sum_v = 0
    cnt = 0
    for f, t, w in edge:
        if find_set(f) != find_set(t):
            union(f, t)
            sum_v += w
            cnt += 1
            if cnt == V:
                break

    print(f'#{tc} {sum_v}')
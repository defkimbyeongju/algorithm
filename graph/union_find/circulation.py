# 해당 노드의 최상위 부모를 찾는 함수
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find_circulation(adj_arr):
    for i in range(N):
        for j in range(i+1, N): # i+1인 이유: 이미 상위 반복에서 해당 값들과 연결을 시켰기 때문에!
            if adj_arr[i][j] == 1:
                if find_set(i) != find_set(j):
                    union(i, j)
                else:
                    return 'WARNING'
    return 'STABLE'

N = int(input())
adj_arr = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N)]
print(find_circulation(adj_arr))

# 최상위 부모 찾는 함수
def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parents[y] = find(x)
    else:
        parents[x] = find(y)


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    parents = [i for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a-1,b-1)
    for i in range(N):
        parents[i] = find(i)
    parents = set(parents)
    print(f'#{tc} {len(parents)}')
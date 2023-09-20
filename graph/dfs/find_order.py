n,m,target = map(int, input().split())
upv = [[] for _ in range(n+1)] # 어떤 학생이 다른 학생보다 잘했는지
downv = [[] for _ in range(n+1)] # 어떤 학생보다 더 잘한 학생

# up: target 보다 못한 학생 수, down : target보다 잘한 학생 수

up = 1
down = 1

upused = [0]*(n+1)
downused = [0]*(n+1)

# target보다 못한 학생들을 탐색하는 dfs 함수
def updfs(node):
    global up
    for next_node in upv[node]: # node보다 못한 학생들 순회
        if not upused[next_node]:
            up += 1
            upused[next_node] = 1
            updfs(next_node)
# target보다 잘한 학생들 탐색 하는 dfs 함수
def downdfs(node):
    global down
    for next_node in downv[node]:
        if not downused[next_node]:
            down += 1
            downused[next_node] = 1
            downdfs(next_node)

for _ in range(m):
    a, b = map(int, input().split())
    upv[b].append(a) # b보다 a가 잘했다는 정보 저장
    downv[a].append(b) # a보다 b가 잘했다는 정보 저장

updfs(target)
downdfs(target)
print(up)
print(n-down+1)
# N, E = 8, 7




text = list(input()) # 노드를 입력 받음
N = len(text)
adj = [list(map(int, input().split())) for _ in range(N)] # 인접 행렬 입력
visited = [False for _ in range(N)]  # 방문 여부를 저장하는 리스트, 처음에는 false로 초기화

def dfs(v):
    print(text[v], end='')  # 현재 방문한 노드 출력
    visited[v] = True

    for i in range(N):
        if adj[v][i] and not visited[i]: # 연결되어 있고, 아직 방문하지 않았다면
            dfs(i)  # 탐색 계속
dfs(0) # 0번 노드부터 시작하여 탐색


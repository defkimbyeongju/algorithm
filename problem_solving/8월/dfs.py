# n = int(input())
# evid = [-1, 0, 0, 1, 2, 4, 4]
# timestamp = [8, 3, 5, 6, 8, 9, 10]
# def dfs(n):
#     s = evid[n]
#     if timestamp[s] < timestamp[n]:
#         dfs(s)
#     else:
#         print(f'{s}번 index(출발)')
#     print(f'{n}번 index({timestamp[n]}시)')
#
# dfs(n)

# 전위, 후위순회
n,k = map(int, input().split())
s = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1

visited = [0]*(n+1)
def dfs_preorder(s):
    visited[s] = 1
    print(s, end=' ')
    for i in range(n, -1, -1):
        if arr[s][i] and not visited[i]:
            dfs_preorder(i)

def dfs_postorder(s):
    visited[s] = 1
    for i in range(n, -1, -1):
        if arr[s][i] and not visited[i]:
            dfs_postorder(i)
    print(s, end=' ')

dfs_preorder(s)
print()
visited = [0]*(n+1)
dfs_postorder(s)



# 컴퓨터 바이러스
# n = int(input()) # 컴퓨터의 수
# k = int(input()) # 노드의 개수
# arr = [list(map(int, input().split())) for _ in range(k)]
# adj_m = [[0]*(n+1) for _ in range(n+1)]
# for i in arr:
#     a, b = i
#     adj_m[a][b] = 1
# visited = [0] * (n+1)
# def dfs(s):
#     visited[s] = 1
#     for i in range(1,n+1):
#         if adj_m[s][i] and not visited[i]: # 연결되어 있고, 아직 방문하지 않은 컴퓨터일 때
#             dfs(i)
# dfs(1)
# print(sum(visited)-1)

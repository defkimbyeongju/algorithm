# BFS version
# N, Q = map(int, input().split())
# arr = [[] for _ in range(N+1)]
# def union(a,b):
#     arr[a].append(b)
#     arr[b].append(a)
#
# def find(a,b):
#     queue = []
#     queue.append(a)
#     visited = [0]*(N+1)
#     visited[a] = 1
#     while queue:
#         t = queue.pop(0)
#         for i in arr[t]:
#             if visited[i] == 0:
#                 queue.append(i)
#                 visited[i] = 1
#     if visited[b]:
#         return 'YES'
#     else:
#         return 'NO'
#
# for _ in range(Q):
#     K, A, B = map(int, input().split())
#     if K == 1:
#         union(A,B)
#     else:
#         print(find(A,B))

# DFS version
# N, Q = map(int, input().split())
# arr = [[0]*(N+1) for _ in range(N+1)]
# def union(a,b):
#     arr[a][b] = 1
#     arr[b][a] = 1
#
# visited = [0]*(N+1)
# def find(a):
#     visited[a] = 1
#     for i in range(1, N+1):
#         if arr[a][i] == 1 and visited[i] == 0:
#                 find(i)
# for _ in range(Q):
#     K, A, B = map(int, input().split())
#     if K == 1:
#         union(A,B)
#     else:
#         find(A)
#         if visited[B]:
#             print("YES")
#         else:
#             print("NO")


# 강사님 풀이

# def find(node):
#     if node != root[node]: # 노드의 부모가 자기 자신이 아니라면
#         root[node] = find(root[node]) # 부모 노드를 찾아간다 -> 경로 압축 수행
#     return root[node]
#
# def union(x,y):
#     root_x = find(x)  # x의 루트 부모 찾기
#     root_y = find(y)  # y의 루트 부모 찾기
#     if rank[root_x] > rank[root_y]: # x의 랭크가 더 크다면 y의 부모를 x의 루트부모로 설정
#         root[root_y] = root_x
#     else:
#         root[root_x] = root_y
#         if rank[root_x] == rank[root_y]: # 만약 랭크가 같다면 y의 랭크 증가
#             rank[root_y] += 1
#
# N,Q = map(int, input().split())
# rank = [0]*(N+1) # 각 노드의 랭크를 저장하는 리스트
# root = [i for i in range(N+1)] # 각 노드의 루트 부모를 저장하는 리스트
# for _ in range(Q):
#     K,A,B = map(int,input().split())
#     if K == 0:
#         if find(A) == find(B):  # A와 B가 같은 그룹에 속하면
#             print('YES')
#         else:
#             print('NO')
#     else:
#         union(A,B) # A와 B를 같은 그룹으로 연결


# 인디언 족장
def find(node):
    if node != root[node]: # 노드의 부모가 자기 자신이 아니라면
        root[node] = find(root[node]) # 부모 노드를 찾아간다 -> 경로 압축 수행
    return root[node]

def union(x,y):
    root_x = find(x)  # x의 루트 부모 찾기
    root_y = find(y)  # y의 루트 부모 찾기
    if rank[root_x] > rank[root_y]: # x의 랭크가 더 크다면 y의 부모를 x의 루트부모로 설정
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]: # 만약 랭크가 같다면 y의 랭크 증가
            rank[root_y] += 1

def idx(a):
    return ord(a)-65

T = int(input())
rank = [0]*26 # 각 노드의 랭크를 저장하는 리스트
root = [i for i in range(26)] # 각 노드의 루트 부모를 저장하는 리스트
for _ in range(T):
    a, b = input().split()
    x, y = idx(a), idx(b)
    union(x, y)

team = 26 - len(set(root))
alone = 0
for i in rank:
    if i == 0:
        alone += 1

print(team)
print(alone)

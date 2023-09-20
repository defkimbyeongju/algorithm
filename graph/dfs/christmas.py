# def pre_order_dfs(i):
#     if i == -1:
#         return
#     print(tree[i][0], end=" ")  # 현재 노드 처리
#     pre_order_dfs(tree[i][1])  # 왼쪽 서브트리 순회
#     pre_order_dfs(tree[i][2])  # 오른쪽 서브트리 순회
#
#
# def in_order_dfs(i):
#     if i == -1:
#         return
#     in_order_dfs(tree[i][1])  # 왼쪽 서브트리 순회
#     print(tree[i][0], end=" ")  # 현재 노드 처리
#     in_order_dfs(tree[i][2])  # 오른쪽 서브트리 순회
#
# def post_order_dfs(i):
#     if tree[i][1] != -1:
#         for j in range(N):
#             if tree[j][0] == tree[i][1]:
#                 post_order_dfs(j)
#     if tree[i][2] != -1:
#         for j in range(N):
#             if tree[j][0] == tree[i][2]:
#                 post_order_dfs(j)
#     print(tree[i][0], end=" ")
#
#
#
#
# N = int(input())
# tree = [list(map(int, input().split())) for _ in range(N)]
# in_order_dfs(0)
# print()
# pre_order_dfs(0)
# print()
# post_order_dfs(0)

tree = [[-1,-1] for _ in range(1001)]
N = 0
preorder = []
inorder = []
postorder = []

def dfs(now):
    if now == -1:
        return
    # 전위순회(루트 -> 왼쪽 -> 오른쪽)
    preorder.append(now)
    # 왼쪽으로 탐색
    dfs(tree[now][0])
    # 중위순회(왼쪽 -> 루트 -> 오른쪽)
    inorder.append(now)
    # 오른쪽으로 탐색
    dfs(tree[now][1])
    # 후위순회(왼쪽 -> 오른쪽 -> 루트)
    postorder.append(now)

N = int(input())
for _ in range(N):
    root, left, right = map(int, input().split())
    tree[root][0] = left
    tree[root][1] = right
dfs(1)

print(' '.join(map(str, inorder)))
print(' '.join(map(str, preorder)))
print(' '.join(map(str, postorder)))

# def dfs(v):
#     visited[v] = 1
#     for i in tree[v]:
#         dfs(i)
#
# T = int(input())
# for tc in range(1,T+1):
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))
#     tree = [[] for _ in range(E+2)]
#     visited = [0] * (E+2)
#     for i in range(E):
#         tree[arr[i*2]].append(arr[i*2+1])
#     dfs(N)
#     print(f'#{tc} {sum(visited)}')


# 강사님 풀이

def sub_tree(node):
    global cnt
    for i in range(2): # 왼쪽, 오른쪽 자식
        if tree[i][node]: # 해당 노드의 자식이 있다면
            cnt += 1
            n = tree[i][node] # 자식 노드의 번호
            sub_tree(n) # 자식 노드에 대해 재귀호출

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    temp = input().split()
    # 노드 번호는 1번 부터 E+1번까지 존재 -> 이진트리 리스트 초기화
    tree = [[0 for _ in range(E+2)] for _ in range(E+2)]
    for i in range(E):
        p_node = int(temp[2*i])  # 부모 노드
        c_node = int(temp[2*i+1]) # 자식 노드 번호 -> 홀수번째
        if tree[0][p_node] == 0:  # 왼쪽 자식이 없다면 할당, 왼쪽자식이 있다면 오른쪽에 할당
            tree[0][p_node] = c_node
        else:
            tree[1][p_node] = c_node
    cnt = 1
    sub_tree(N)
    print(f'#{tc} {cnt}')

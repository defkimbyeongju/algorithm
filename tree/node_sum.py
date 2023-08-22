# def node_sum(n):
#     while n > 0:
#         if n*2 <= N:
#             tree[n] += tree[n*2]
#         if n*2+1 <= N:
#             tree[n] += tree[n*2+1]
#         n -= 1
#
# T = int(input())
# for tc in range(1,T+1):
#     N, M, L = map(int, input().split())
#     tree = [0 for _ in range(N+1)]
#     for _ in range(M):
#         a,b = map(int,input().split())
#         tree[a] = b
#     for i in range(N, 0, -1):
#         if tree[i] == 0:
#             start = i
#             break
#     node_sum(start)
#     print(f'#{tc} {tree[L]}')


# 강사님 풀이
T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value # 트리에 리프 노드 값을 저장
    for i in range(N,0,-1):
        if i//2 > 0: # 부모 노드의 인덱스가 0보다 크다면
            tree[i//2] += tree[i] # 부모 노드에 자식 노드 값을 더함
    result = tree[L]
    print(f'#{tc} {result}')

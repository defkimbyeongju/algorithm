'''
def inorder(p, N): # N 완전이진트리의 마지막 정점
    if p<=N:
        inorder(p*2,N)  # 왼쪽 자식으로 이동
        print(tree[p], end ='')
        inorder(p*2+1,N)  # 오른쪽 자식으로 이동


T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1) # N번 노드까지 있는 완전이진트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위순회
    print(f'#{tc}', end='')
    inorder(1,N)
    print()
'''
def deq():
    global last
    tmp = heap[1] # 루트 백업
    heap[1] = heap[last]  # 삭제할 노드의 키를 루트에 복사
    last -= 1 # 마지막 노드 삭제
    p = 1 # 루트에 옮긴 값을 자식과 비교
    c = p*2 # 왼쪽 자식(비교할 자식노드 번호)
    while c <= last: # 자식이 하나라도 있으면...
        if c+1 <= last and heap[c] < heap[c+1]:  # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1  # 비교 대상이 오른쪽 자식 노드
        if heap[p] < heap[c]: # 자식이 더 크면 최대합ㄴ 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c # 자식을 새로운 부모로
            c = p*2  # 왼쪽 자식 번호를 계산
        else: # 부모가 더 크면 비교 중단
            break
    return tmp
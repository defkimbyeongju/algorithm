# def binary_heap():

# 큐: 선입선출
# 우선순위 큐: 데이터를 우선순위를 가지고 저장, 우선순위가 높은 것부터 꺼냄
# 힙: 우선순위 큐를 구현하는 트리 기반의 자료구조, 최대힙, 최소힙
# import heapq -> heapq 라이브러리를 사용하여 최소 힙을 구현
# heapq.heappush(heap,num): num을 최소 힙에 삽입
# heapq.heappop(heap): 최소 힙 heap에서 가장 작은 값을 꺼내서 반환

# import heapq
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     tree = []
#     number = map(int, input().split())
#     for num in number:
#         heapq.heappush(tree, num)
#     sum_v = 0
#     N = len(tree) // 2
#     while N:
#         sum_v += tree[N-1]
#         N //=2
#     print(f'#{tc} {sum_v}')

def binary_heap(n):
    if n > 1:
        if heap[n] < heap[n//2]:
            heap[n//2], heap[n] = heap[n], heap[n//2]
            binary_heap(n//2)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    heap = [0 for _ in range(N+1)]
    arr = list(map(int, input().split()))
    for i in range(N):
        heap[i+1] = arr[i]
        if heap[(i+1)//2]:
            binary_heap(i+1)
    total = 0
    while N > 1:
        N //=2
        total += heap[N]
    print(f'#{tc} {total}')


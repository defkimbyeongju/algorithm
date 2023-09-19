import heapq
N = int(input())
max_heap = [(-500,500)]
min_heap = []
for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        heapq.heappush(max_heap, (-a,a))
        heapq.heappush(min_heap, b)
    else:
        heapq.heappush(max_heap, (-b, b))
        heapq.heappush(min_heap, a)

    if max_heap[0][1] > min_heap[0]:
        p1 = heapq.heappop(max_heap)[1]
        p2 = heapq.heappop(min_heap)
        p2 = (-p2, p2)
        heapq.heappush(max_heap, p2)
        heapq.heappush(min_heap, p1)
    print(max_heap[0][1])
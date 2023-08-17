# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     q = [0] * (N + M)
#     front = 0
#     rear = N-1
#     for i in range(N):
#         q[i] = arr[i]
#     for i in range(1,M+1):
#         q[i+rear] = q[front]
#         front += 1
#     print(f'#{tc} {q[front]}')

N = int(input())//90

front = 0
rear = 0
arr = [3,12,9,6]
k = len(arr)
q = [0]*k

def enqueue(item):
    global rear
    rear = (rear+1) % k
    q[rear] = item

def dequeue():
    global front
    front = (front+1) % k
    return q[front]

for i in arr:
    enqueue(i)

for j in range(N):
    a = dequeue()
    enqueue(a)

print(q)
# 슬라이딩 윈도우
# 1. 주로 리슽으와 같은 시퀀스타입에서 일정 크기의 윈도우를 정한다.
# 2. 그 윈도우를 데이터의 처음부터 끝까지 움직이면서 해결한다.
'''
n개의 정수를 입력받고, 연속된 m개의 정수들의 합을 구할 때 최대값 구하기
합이 가장 큰 구간의 값은 무엇일까요? (2 <= m,n <= 100,000)
input
10 2
3 -2  -4 -9 0 3 7 13 8 -3
output
21
N,M = map(int, input().split())
arr = list(map(int, input().split()))
total = 0


for i in range(M):
    total += arr[i]
    max_v = total
for i in range(N-M):
    total += arr[i+M]
    total -= arr[i]
    if max_v < total:
        max_v = total

print(max_v)
'''



# 투 포인터(Two Pointer)
# 주로 리스트와 같은 시퀀스 타입에서 두개의 포인터를 사용하여 문제를 풀이하는 방법

'''
1부터 10000사이의 n개의 자연수 중에서 연속된 숫자를 더했을 때 합이 m이 되는 경우는 몇가지인가요?
(투포인터 -> 구간의 크기가 정해지지 않음)

input
10 5
1 2 3 4 2 5 3 1 1 2


output
3

n,target = map(int, input().split())
arr = list(map(int, input().split()))
cnt,sum = 0, 0
# 투 포인터 high, low
high, low = 0, 0
while True:
    if sum >= target or high == n:
        sum -= arr[low]
        low += 1
    elif sum < target:
        sum += arr[high]
        high += 1
    if sum == target:
        cnt += 1
    if low == n:
        break
print(cnt)
'''


# T = int(input())
# for tc in range(1,T+1):
#     n, w = map(int, input().split())
#     arr = list(map(int, input().split()))
#     total = 0
#     start,end = 0, w-1
#     for i in range(w):
#         total += arr[i]
#         max_v = total
#
#     for i in range(n-w):
#         total += arr[i+w]
#         total -= arr[i]
#         if max_v < total:
#             max_v = total
#             start = i+1
#             end = i+w
#     print(f'#{tc} {start} {end} {max_v}')


# n, target = map(int, input().split())
# arr = list(map(int, input().split()))
# total, cnt = 0, 0
# high, low = 0, 0
# while True:
#     if total >= target or high == n:
#         total -= arr[low]
#         low += 1
#     elif total < target:
#         total += arr[high]
#         high += 1
#     if total == target:
#         cnt += 1
#     if low == n:
#         break
# print(cnt)





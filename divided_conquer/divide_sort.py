# from collections import deque
#
# def merge(left, right):
#     global cnt
#     result = []
#     if left[-1] > right[-1]:
#         cnt += 1
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left.popleft())
#             else:
#                 result.append(right.popleft())
#         elif len(left) > 0:
#             result.append(left.popleft())
#         elif len(right) > 0:
#             result.append(right.popleft())
#     return result
#
# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     left = deque()
#     right = deque()
#     mid = len(arr) // 2
#     for i in range(mid):
#         left.append(arr[i])
#     for i in range(mid, len(arr)):
#         right.append(arr[i])
#
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     return merge(left, right)
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     cnt = 0
#     res = merge_sort(numbers)
#     print(f'#{tc} {res[N//2]} {cnt}')


# 강사님 풀이

def divide(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = divide(arr[:middle])
    right = divide(arr[middle:])
    return merge(left, right) # 두 부분 병합

def merge(left, right):
    global cnt
    # 왼쪽 리스트의 마지막 원소가 오른쪽 리스트의 마지막 원소보다 큰 경우 cnt 1 증가
    if right[-1] < left[-1]:
        cnt += 1
    result = [] # 병합결과
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:
        # 왼쪽과 오른쪽 리스트 모두 남아 있는 경우
        if l < len_l and r < len_r:
            if left[l] <= right[r]:
                result.append(left[l]) # 왼쪽의 원소를 result에 추가
                l += 1
            else:
                result.append(right[r]) # 반대의 경우 오른쪽 원소를 추가
                r += 1
        # 왼쪽 리스트만 남아 있는 경우
        elif l < len_l:
            result.append(left[l])
            l += 1
        # 오른쪽 리스트만 남아 있는 경우
        elif r < len_r:
            result.append(right[r])
            r += 1
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    res = divide(numbers)
    print(f'#{tc} {res[N//2]} {cnt}')
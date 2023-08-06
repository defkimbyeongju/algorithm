# 버블정렬 실습
#
# numbers = [63, 31, 27, 11, 25]
#
# def bubble(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# bubble(numbers)
# print(numbers)


# 카운팅 정렬: 정수를 정렬하는 알고리즘, 각 숫자의 개수를 세어서 정렬

# def counting(arr):
#     max_value = max(arr)
#     count_arr = [0] * (max_value + 1)
#     for num in arr:
#         count_arr[num] += 1
#     sorted_arr = []
#     for i, count in enumerate(count_arr):
#         sorted_arr.extend([i] * count)  # iterable 증가시키기
#     return sorted_arr
# list1 = [1, 4, 1, 2, 7, 5, 2]
# sorted_arr = counting(list1)
# print(sorted_arr)


# 순열: 주어진 항목들로 만들 수 있는 모든 가능한 순서(튜플)
# itertools 모듈 사용
# import itertools
#
# numbers = [1, 2, 3, 4, 5]
# p = itertools.permutations(numbers)
# c = itertools.combinations(numbers, 2)
# print(list(p))

# 그리디 알고리즘: 각 단계에서 가장 최선의 선택을 하는 방법
# 거스름돈을 줄 때 가장 적은 수의 동전을 사용하여 거스름돈을 주는 문제
# 최선의 선택: 가장 큰 단위의 동전부터 사용
# 실습 : 동전 종류가 100, 50, 10 거스름돈이 380원이라면, 어떻게 해야 가장 적은 수의 동전으로 거스름돈을 받을 수 있을까요?



# def money(n, coins):
#     coins.sort(reverse=True)
#     change = {coin : 0 for coin in coins}
#     for coin in coins:
#         while n >= coin:
#             n -= coin
#             change[coin] += 1
#     return change
#
# result = money(380, [100, 50, 10])
#



# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input()))
#     arr = [0] * 10
#     max_v = 0
#     max_idx = 0
#     for i in numbers:
#         arr[i] += 1
#     for j in range(len(arr)):
#         if max_v < arr[j]:
#             max_v = arr[j]
#             max_idx = j
#         elif max_v == arr[j]:
#             max_idx = j
#     print(f'#{tc} {max_idx} {max_v}')
#

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    for i in range(N):
        if i % 2 == 0:
            new_arr.append(max(arr))
            arr.remove(max(arr))
        else:
            new_arr.append(min(arr))
            arr.remove(min(arr))
    print(f'#{tc}', *new_arr[:10])

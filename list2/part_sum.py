# T = int(input())
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for tc in range(1, T+1):
#     N, K = map(int,input().split())
#     result = 0
#     # 1<<12 -> 이진수 1을 왼쪽으로 12비트 이동 -> 1000000000000 -> 2**12
#     for i in range(1<<12):
#         sum_sub = 0
#         subset = []
#         for j in range(12):
#             # i의 j번째 비트가 1인지 아닌지 알 수 있다.
#             # 12의 이진수 1100, 5의 이진수 0101 -> 1100 & 0101 -> 0100
#             if i & (1<<j):
#                 sum_sub += A[j]
#                 subset.append(A[j])
#
#         if len(subset) == N and sum_sub == K:
#             result += 1
#
#     print(f'#{tc} {result}')

'''
def binary_search(pages, p):
    start = 1
    end = pages
    mid = 0
    cnt = 1
    #만약 middle이 p와 같다면, 찾는 값 p를 찾은 것이므로 탐색을 종료
    while p != mid:
        mid = (end + start) // 2
        if mid > p:
            end = mid
        else:
            start = mid
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())
    a = binary_search(p, pa)
    b = binary_search(p, pb)
    result = 0
    if a==b:
        result = 0
    elif a < b:
        result = 'A'
    else:
        result = 'B'
    print(f'#{tc} {result}')
'''

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []

    while len(numbers)>0:
        max_value = max(numbers)
        numbers.remove(max_value)
        result.append(max_value)

        min_value = min(numbers)
        numbers.remove(min_value)
        result.append(min_value)
    print(f'#{tc}' ,*result[:10])
'''

# T = int(input())
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for tc in range(1, T+1):
#     N, K = map(int,input().split())
#     result = 0
#
#     for i in range(1<<12): # 집합의 원소 개수만큼
#         sum_sub = 0
#         subset = []
#         for j in range(12):
#             # i의 j번째 비트가 1인지 아닌지 알 수 있다.
#             # 12의 이진수 1100, 5의 이진수 0101 -> 1100 & 0101 -> 0100
#             if i & (1<<j): # i는 이진수로 변환하면 0000, 0001, 0010, 0011, 0100 ... 과 같은 식으로 쭉 증가할 것이다. 그 때마다, 각 자리수를 비교해서 j는 0001, 0010, 0100, 1000과 같은 식으로 반복하며, 해당 요소가 존재하면 그 인덱스를 리스트에 추가하는 방식으로 모든 부분집합을 만들 수 있다.
#                 sum_sub += A[j]
#                 subset.append(A[j])
#         if sum_sub == K and len(subset) == N:
#             result += 1
#     print(f'#{tc} {result}')



# T = int(input())
# A = [i for i in range(1, 13)]
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     result = 0
#     for i in range(1<<12):
#         sum_sub = 0
#         subset = []
#         for j in range(12):
#             if i & (1<<j):
#                 sum_sub += A[j]
#                 subset.append(A[j])
#         if sum_sub == K and len(subset) == N:
#             result += 1
#     print(f'#{tc} {result}')


T = int(input())

for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    l = 1
    r = p
    total_a = 0
    total_b = 0
    c = 0
    while c != a:
        c = int((l + r) / 2)
        if c < a:
            l = c
        else:
            r = c
        total_a += 1
    l = 1
    r = p
    c=0
    while c != b:
        c = int((l + r) / 2)
        if c < b:
            l = c
        else:
            r = c
        total_b += 1
    if total_a < total_b:
        print(f'#{tc} A')
    elif total_a > total_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')








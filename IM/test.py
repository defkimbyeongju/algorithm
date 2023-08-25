# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     max_lst = []
#     for i in range(N-1):
#         temp = 0
#         danjo = str(numbers[i]*numbers[i+1])
#         if len(danjo) == 1:
#             temp = -1
#         else:
#             for j in range(len(danjo)-1):
#                 if danjo[j] > danjo[j+1]:
#                     temp = -1
#                     break
#                 else:
#                     temp += 1
#         if temp != -1:
#             max_lst.append(int(danjo))
#
#     if not max_lst:
#         print(f'#{tc}',-1)
#     else:
#         print(f'#{tc} {max(max_lst)}')


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     max_result = -1  # 변수명 변경 및 초기화
#
#     for i in range(N-1):
#         for j in range(i+1, N):  # 모든 숫자 쌍의 곱을 고려
#             danjo = str(numbers[i] * numbers[j])
#             is_danjo = True
#
#             for k in range(len(danjo)-1):
#                 if danjo[k] > danjo[k+1]:
#                     is_danjo = False
#                     break
#
#             if is_danjo:
#                 max_result = max(max_result, int(danjo))
#
#     print(f'#{tc} {max_result}')


# 369 게임

# N = int(input())
# three = ['3', '6', '9']
# numbers = [str(i) for i in range(1,N+1)]
#
# for i in numbers:
#     cnt = 0
#     for j in i:
#         if j in three:
#             cnt += 1
#
#     if cnt == 0:
#         print(int(i), end=' ')
#     else:
#         print('-'*cnt, end =' ')

# 농작물

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     total = 0
#     start, end = N // 2 , N // 2
#     for i in range(N):
#         for j in range(start, end+1):
#             total += arr[i][j]
#         if i < N // 2:
#             start -= 1
#             end += 1
#         else:
#             start += 1
#             end -= 1
#     print(f'#{tc} {total}')


# 마그네틱
# T = 10
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         stack = []
#         for j in range(N):
#             if arr[j][i] != 0:
#                 stack.append(arr[j][i])
#
#         while True:
#             t = stack.pop()
#             if len(stack) == 0:
#                 break
#             if t == 1:
#                 continue
#             if t != stack[-1]:
#                 cnt += 1
#
#
#     print(f'#{tc} {cnt}')


# 문자열 마디
# T = int(input())
# for tc in range(1,T+1):
#     word = list(input())
#     for i in range(10, -1, -1):
#         if word[:i] == word[i:i+i]:
#             if i % 2 == 0:
#                 if word[:i//2] == word[i//2:i]:
#                     if (i//2) % 2 == 0 and word[:(i//2)//2] == word[(i//2)//2:i//2]:
#                         result = (i//2)//2
#                         break
#                     else:
#                         result = i//2
#                         break
#                 else:
#                     result = i
#                     break
#             if i % 3 == 0:
#                 if word[:i//3] == word[i//3:i//3+i//3]:
#                     result = i//3
#                     break
#                 else:
#                     result = i
#                     break
#             else:
#                 result = i
#                 break
#     print(f'#{tc} {result}')


# 스도쿠 검증

# def sudoku(arr):
#     for i in range(9): # 가로 검증
#         if len(set(arr[i])) != 9:
#             return 0
#
#     for i in range(9): # 세로 검증
#         temp = []
#         for j in range(9):
#             temp.append(arr[j][i])
#         if len(set(temp)) != 9:
#             return 0
#
#     for i in range(0,7,3): # 대각
#         for j in range(0,7,3):
#             tmp = []
#             tmp.append(arr[i][j:j+3])
#             tmp.append(arr[i+1][j:j+3])
#             tmp.append(arr[i+2][j:j+3])
#         tmp = sum(tmp,[])
#         if len(set(tmp)) != 9:
#             return 0
#
#     return 1
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     arr = [list(map(int,input().split())) for _ in range(9)]
#     print(f'#{tc} {sudoku(arr)}')


# 빵준이 카드게임

# def card(card_list):
#     S = [[] for _ in range(14)]
#     D = [[] for _ in range(14)]
#     H = [[] for _ in range(14)]
#     C = [[] for _ in range(14)]
#     for i in range(0,len(card_list)-2,3):
#         idx = ''
#         idx += card_list[i + 1]
#         idx += card_list[i + 2]
#         idx = int(idx)
#         if card_list[i] == 'S':
#             if not S[idx]:
#                 S[idx].append(1)
#             else:
#                 return 'ERROR'
#         elif card_list[i] == 'D':
#             if not D[idx]:
#                 D[idx].append(1)
#             else:
#                 return 'ERROR'
#         elif card_list[i] == 'H':
#             if not H[idx]:
#                 H[idx].append(1)
#             else:
#                 return 'ERROR'
#         else:
#             if not C[idx]:
#                 C[idx].append(1)
#             else:
#                 return 'ERROR'
#     s = 13 - sum(sum(S, []))
#     d = 13 - sum(sum(D, []))
#     h = 13 - sum(sum(H, []))
#     c = 13 - sum(sum(C, []))
#     return s, d, h, c
#
#
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     card_list = list(input())
#     t = card(card_list)
#     if t == 'ERROR':
#         print(f'#{tc} {t}')
#     else:
#         print(f'#{tc}', *t)

# 퍼펙트 셔플

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(input().split())
    front = []
    rear = []
    if N % 2 == 0:
        for i in range(N//2):
            front.append(card.pop(0))
        for j in range(N//2, N):
            rear.append(card.pop(0))
        while True:
            card.append(front.pop(0))
            if not front and not rear:
                break
            card.append(rear.pop(0))
            if not front and not rear:
                break
        print(f'#{tc}', *card)
    else:
        for i in range(N//2+1):
            front.append(card.pop(0))
        for j in range(N//2+1, N):
            rear.append(card.pop(0))
        while True:
            card.append(front.pop(0))
            if not front and not rear:
                break
            card.append(rear.pop(0))
            if not front and not rear:
                break
        print(f'#{tc}', *card)

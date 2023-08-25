T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ci = list(map(int, input().split()))
    ci.sort()
    carrot = [] # 당근의 포장 조건을 만족하는 개수 차이
    for i in range(1, N-1):  # 첫번째 상자와 두번째 상자 사이
        for j in range(i+1, N): # 두번째 상자와 세번째 상자 사이
            A = ci[:i] # 첫번째 상자
            B = ci[i:j] # 두번째 상자
            C = ci[j:] # 세번째 상자
            if A[-1] == B[0] or B[-1] == C[0]: # 같은 크기의 당근이 인접한 상자에 있으면
                continue
            if len(A) * len(B) * len(C) == 0: # 빈 상자가 있으면
                continue
            if len(A) > N//2 or len(B) > N//2 or len(C) > N//2:
                continue
            # 상자 간의 당근 개수 차이
            carrot.append(max(abs(len(A) - len(B)),abs(len(B) - len(C)), abs(len(C) - len(A))))
    try:
        print(f'#{tc} {min(carrot)}')

    except:
        print(f'#{tc} -1')







# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     carrot = list(map(int, input().split()))
#     carrot.sort()
#     lst = []
#     lst_2 = []
#     while True:
#         if carrot:
#             s = carrot.count(carrot[0])
#             if s + len(lst) <= N// 2:
#                 for i in range(s):
#                     lst.append(carrot.pop(0))
#                 else:
#                     break
#             else:
#                 if s + len(lst) <= N // 2:
#                     for i in range(s):
#                         lst.append(carrot.pop(0))
#                 else:
#                     break
#         else:
#             break
#     while True:
#         if carrot:
#             s = carrot.count(carrot[0])
#             if s == 1:
#                 if s + len(lst_2) <= (N // 3) + (N % 3) // 2:
#                     for i in range(s):
#                         lst_2.append(carrot.pop(0))
#                 else:
#                     break
#             else:
#                 if s + len(lst_2) <= N// 2:
#                     for i in range(s):
#                         lst_2.append(carrot.pop(0))
#                 else:
#                     break
#         else:
#             break
#
#     if len(lst) > N//2 or len(lst_2) > N//2 or len(carrot) > N//2 or min(len(lst), len(lst_2), len(carrot)) == 0:
#         result = -1
#     else:
#         result = max(len(lst), len(lst_2), len(carrot)) - min(len(lst), len(lst_2), len(carrot))
#
#     print(f'#{tc} {result}')
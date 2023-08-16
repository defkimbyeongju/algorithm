# def forth(num):
#     oper = ['*', '/', '+', '-']
#     stack = []
#     for i in num:
#         if i in oper:
#             if len(stack) < 2:
#                 return 'error'
#             else:
#                 a = int(stack.pop())
#                 b = int(stack.pop())
#                 if i == '+':
#                     tmp = a+b
#                     stack.append(tmp)
#                 elif i == '-':
#                     tmp = b-a
#                     stack.append(tmp)
#                 elif i == '/':
#                     tmp = b//a
#                     stack.append(tmp)
#                 elif i == '*':
#                     tmp = a*b
#                     stack.append(tmp)
#         elif i == '.':
#             if len(stack) != 1:
#                 return 'error'
#             else:
#                 return stack.pop()
#         else:
#             stack.append(i)
#
# T = int(input())
# for tc in range(1,T+1):
#     num_list = input().split(' ')
#     print(f'#{tc} {forth(num_list)}')


# 강사님 풀이
T = int(input())
for tc in range(1,T+1):
    forth = list(input().split())
    stack = []
    error = False
    for i in range(len(forth)-1):
        if forth[i].isdigit():
            stack.append(forth[i])
        else:  # 연산자일 경우 -> 연산 결과를 스택에 추가
            try:
                b = int(stack.pop())  # 두번째 숫자
                a = int(stack.pop())  # 첫번째 숫자
                if forth[i] == '+':
                    stack.append(a+b)
                elif forth[i] == '-':
                    stack.append(a + b)
                elif forth[i] == '*':
                    stack.append(a * b)
                elif forth[i] == '/':
                    stack.append(a//b)
            except:  # 두 개의 숫자를 꺼낼 수 없는 경우
                error = True

    if error == True or len(stack) != 1:
        print(f'#{tc}error')
    else:
        print(f'#{tc} {stack.pop()}')

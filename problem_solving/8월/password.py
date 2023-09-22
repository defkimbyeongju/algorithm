# for tc in range(1, 11):
#     N, password = input().split()
#     stack = list(password)
#     temp = 0
#     for i in range(1, int(N)):
#         if len(stack) == 0:
#             stack.append(password[i])
#         if stack.pop() == temp[i]:
#             stack.pop()
#         else:
#             stack.append(temp[i])
#     print(f'#{tc} {stack}')


# 라이브 강사 풀이
for tc in range(1, 11):
    N, password = input().split()
    N = int(N)
    stack = [0] * N
    top = -1

    for t in password:
        if top == -1 or stack[top] != t:
            top += 1
            stack[top] = t
        else:      # 스택이 비어있지 않고, top과 같으면
            top -= 1
    text = ''.join(stack[:top+1])
    print(f'#{tc} {text}')
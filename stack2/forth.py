def forth(num):
    oper = ['*', '/', '+', '-']
    stack = []
    for i in num:
        if i in oper:
            if len(stack) < 2:
                return 'error'
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == '+':
                    tmp = a+b
                    stack.append(tmp)
                elif i == '-':
                    tmp = b-a
                    stack.append(tmp)
                elif i == '/':
                    tmp = b//a
                    stack.append(tmp)
                elif i == '*':
                    tmp = a*b
                    stack.append(tmp)
        elif i == '.':
            if len(stack) != 1:
                return 'error'
            else:
                return stack.pop()
        else:
            stack.append(i)

T = int(input())
for tc in range(1,T+1):
    num_list = input().split(' ')
    print(f'#{tc} {forth(num_list)}')

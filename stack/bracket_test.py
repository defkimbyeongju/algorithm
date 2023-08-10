T = int(input())
for tc in range(1,T+1):
    text = input()
    stack_list = []
    result = 1
    for i in text:
        if i == '(' or i == '{' or i == '[':
            stack_list.append(i)
        if i == ')':
            if len(stack_list) == 0:
                result = 0
                break
            else:
                if stack_list.pop() != '(':
                    result = 0
                    break
        if i == '}':
            if len(stack_list) == 0:
                result = 0
                break
            else:
                if stack_list.pop() != '{':
                    result = 0
                    break
        if i == ']':
            if len(stack_list) == 0:
                result = 0
                break
            else:
                if stack_list.pop() != '[':
                    result = 0
                    break
    if len(stack_list) != 0:
        result = 0
    print(f'#{tc} {result}')
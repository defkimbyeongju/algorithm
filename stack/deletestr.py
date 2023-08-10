T = int(input())

for tc in range(1,T+1):
    text = input()
    stack = []
    for i in text:
        if i not in stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    print(f'#{tc} {len(stack)}')
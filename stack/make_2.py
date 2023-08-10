def binary(n):
    # 재귀함수 종료조건
    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    # 1보다 큰 경우
    else:
        # n을 2로 나눈 몫을 재귀호출, 나머지를 문자열로 더한다
        return binary(n//2) + str(n%2)

N = int(input())
print(binary(N))


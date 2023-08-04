# 방향배열은 이제 좀 적응한듯

''' input
5
1 2 3 5 10
9 7 2 2 9
0 0 1 5 7
5 2 3 2 2
1 1 1 1 1
2

결과는 26이 출력되어야 함!
'''

'''
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

max_v = 0
for i in range(N):
    for j in range(N):
        count = 0
        for p in range(4):
            for k in range(1, K+1):
                ni, nj = i+di[p]*k, j+dj[p]*k
                if 0<= ni < N and 0<= nj < N:
                    count += arr[ni][nj]
        if max_v < count:
            max_v = count

print(max_v)
'''

# 강사님 풀이
N = int(input())
arr = []
a = 0
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)

K = int(input())

def magic(y, x):
    dy = [-1, 1, -1, 1]
    dx = [1, 1, -1, -1]
    result = 0
    # 마법의 범위가 4방향
    for i in range(4):
        # 마법의 파워
        for j in range(1, K+1):
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if 0<=ny<N and 0<=nx<N:
                result += arr[ny][nx]
    return result
result_list = []
for i in range(N):
    for j in range(N):
        result_list.append(magic(i, j))
print(max(result_list))

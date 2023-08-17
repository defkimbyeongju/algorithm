# def recursion(s, l, r):
#     global total
#     total += 1
#     if l >= r:
#         return 1
#     elif s[l] != s[r]:
#         return 0
#     else:
#         return recursion(s, l+1, r-1)
#
# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)
#
# T = int(input())
# for _ in range(T):
#     total = 0
#     text = input()
#     print(isPalindrome(text), total)

# text = [list(input()) for _ in range(5)]
# ans = ''
# max_v = 0
# for i in text:
#     if max_v < len(i):
#         max_v = len(i)
# for i in range(max_v):
#     for j in range(5):
#         if len(text[j]) > i:
#             ans += text[j][i]
#         else:
#             continue
# print(ans)

# 이것이 코딩테스트다 dfs 테스트 문제
def dfs(y,x):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    for k in range(4):
        ny, nx = dy[k]+y, dx[k]+x
        if 0<=ny<N and 0<=nx<M:
            if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dfs(ny,nx)

N, M = map(int,input().split())
cnt = 0
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            dfs(i,j)
            cnt += 1
print(cnt)


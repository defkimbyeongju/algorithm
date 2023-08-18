# swea 수학 게임 페스티벌 문제

def double(x):
    return (x*2) % 10000

def subtract(x):
    return x-1 if x != 0 else 9999

def left(x):
    a = str(x).zfill(4)
    a = a[1:] + a[0]
    return int(a)
def right(x):
    a = str(x).zfill(4)
    a = a[3] + a[:3]
    return int(a)


def bfs(a,b):
    dslr = ["d", "s", "l", "r"]
    visited = [''] * 10001
    visited[a] = 'a'
    queue = []
    queue.append(a)
    result = []
    while queue:
        t = queue.pop(0)
        if t == b:
            result.append(visited[t])
            continue
        d, s, l, r = double(t), subtract(t), left(t), right(t)
        if visited[d] == '':
            visited[d] = visited[t] + 'D'
            queue.append(d)
        if visited[s] == '':
            visited[s] = visited[t] + 'S'
            queue.append(s)
        if visited[l] == '':
            visited[l] = visited[t] + 'L'
            queue.append(l)
        if visited[r] == '':
            visited[r] = visited[t] + 'R'
            queue.append(r)

    return result



N = int(input())
for _ in range(N):
    A, B = map(int,input().split())
    res = bfs(A,B)
    min_v = 21e8
    for i in res:
        if len(i) < min_v:
            min_v = len(i)
            ans = i
    print(i[1:])

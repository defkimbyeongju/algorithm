S = int(input())
D = int(input())
adj_lst = ['a','b','c','d']
def bfs(s,g):
    result = []
    visited = [0]*100001
    queue = []
    visited[s]=1
    queue.append(s)
    while queue:
        t = queue.pop(0)
        if t == g:
            result.append(visited[t]-1)
            continue
        for w in adj_lst:
            if w == 'a':
                a = t//2
                if 0 <= a <= 100000:
                    if visited[a] ==0:
                        visited[a] = visited[t]+1
                        queue.append(a)
            elif w == 'b':
                b = t*2
                if 0 <= b <= 100000:
                    if visited[b] == 0 and t < g:
                        visited[b] = visited[t]+1
                        queue.append(b)
            elif w=='c':
                c = t+1
                if 0 <= c <= 100000:
                    if visited[c] == 0 and t < g:
                        visited[c] = visited[t]+1
                        queue.append(c)
            elif w=='d':
                d = t-1
                if 0 <= d <= 100000:
                    if visited[d] == 0:
                        visited[d] = visited[t]+1
                        queue.append(d)
    return result

print(min(bfs(S,D)))
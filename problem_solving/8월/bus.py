T = int(input())
for tc in range(1, T+1):
    count = [0] * 5001
    N = int(input())
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi+1):
            count[i] += 1
    P = int(input())
    count_list = [count[int(input())] for _ in range(P)]
    print(f'#{tc}', *count_list)
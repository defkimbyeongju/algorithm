import copy
def work(arr, primary):
    global min_v
    for i in range(N):
        work_time = 0
        temp_arr = arr[:]
        temp_arr[i] //= 2
        used = [0] * N
        prima = copy.deepcopy(primary)
        while True: # 각각의 업무를 코코가 도와준다고 미리 가정하고 업무 시작!
            min_time = 1001
            for j in range(N):
                if prima[j]: # 사전업무가 있다면
                    for k in range(len(prima[j])):
                        if used[prima[j][k]-1] != -1: # 사전 업무가 안됐다면 얘는 지금 수행 못하니까 넘겨
                            break
                    else: # for - else 문은 break되지 않고 넘어감. 사전업무가 모두 수행됐다면
                        for _ in range(len(prima[j])):
                            prima[j].pop()
                if not prima[j] and temp_arr[j] != 0:
                    used[j] = 1
                    min_time = min(min_time, temp_arr[j])
            if min_time == 1001:
                break
            else:
                work_time += min_time
            for idx in range(N):
                if used[idx] == 1:
                    temp_arr[idx] -= min_time
                    if temp_arr[idx] == 0:
                        used[idx] = -1

        if 0 not in used:
            min_v = min(min_v, work_time)
        else:
            break


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work_list = []
    priority = []
    for _ in range(N):
        temp = list(map(int,input().split()))
        work_list.append(temp[0])
        priority.append(temp[2:])
    min_v = 21e8
    work(work_list, priority)
    if min_v == 21e8:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {min_v}')

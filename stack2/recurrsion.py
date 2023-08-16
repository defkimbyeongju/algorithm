# def f(i,N):
#     if i == N:
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, N)
#         return
# N = 3
# A = [1,2,3]
# B = [0] * N
# f(0,N)
# print(B)
'''
def f(i,N):
    if i == N:
        print(bit, end= ' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end=' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1
        f(i+1,N)
        bit[i]=0
        f(i+1,N)
        return
A = [1,2,3]
bit=[0]*3
f(0,3)
'''

def f(i, N, s, t):  # s: i-1원소까지 부분집합의 합(포함된 원소의 합), t: 찾으려는 합
    global cnt
    cnt += 1
    if s == t:  # 합이 목표치에 도달했다면
        print(bit)
    elif i==N:  # 남은 원소가 없는 경우
        return
    elif s > t:
        return
    else:
        bit[i] = 1
        f(i+1, N, s+A[i], t)
        bit[i] =0
        f(i+1, N, s, t)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우
N = 10
A = [i for i in range(1, N+1)]
bit = [0]*N
cnt = 0
f(0, N, 0, 10)
print(cnt)
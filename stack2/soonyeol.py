# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N): # 자신부터 오른쪽 끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i]
#
#
# A = [0, 1, 2]
# f(0, 3)

def f1(b,e):
    if b==0:
        return 1
    r =1
    for i in range(e):
        r *=b
    return r
def f2(b, e):
    if b==0 or e==0:
        return 1
    if e%2:
        r = f2(b, (e-1)//2)
        return r*r*b
    else:
        r = f2(b, e//2)
        return r*r
print(f1(2,10))
print(f2(2,10))
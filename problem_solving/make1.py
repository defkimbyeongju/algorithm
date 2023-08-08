N = int(input())
result = 0
if N == 1:
    result = 0
while N != 1:
    if N % 3 == 0:
        N /= 3
    elif N % 2 ==0:
        if (N-1) % 3 == 0:
            N -= 1
        else:
            N /= 2
    else:
        N -= 1
    result += 1
print(result)
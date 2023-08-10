def collatz(n):
    total = 0
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            return collatz(n/2) + 1
        else:
            return collatz(n*3+1) +1

N= int(input())
print(collatz(N))



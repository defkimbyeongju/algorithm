def year(x):
    result = 1
    if x == 'XXXX':
        result = 1
    else:
        if x[0] == 'X':
            result *= 9
        if x[1] == 'X':
            result *= 10
        if x[2] == 'X':
            result *= 10
        if x[3] == 'X':
            result *= 10
    return result

def month(y):
    result = 1
    if len(y) == 2:
        if y == 'XX':
            result *= 3
        elif y[0] == 'X':
            result *= 1
        elif y[1] == 'X':
            result *= 3
    if y == 'X':
        result *= 9
    return result

def day(z):
    result = 1
    if len(z) == 2:
        if z == 'XX':
            result *= 22
        elif z[0] == 'X':
            if z[1] == '1' or z[1] == '0':
                result *= 3
            else:
                result *= 2
        elif z[1] == 'X':
            if z[0] == '3':
                result *= 2
            else:
                result *= 10
    return result

date = input().split('.')
total = year(date[0]) * month(date[1]) * day(date[2])
print(total)


def persistence(n):
    r = 0
    while n >= 10:
        y = 1
        x = str(n)
        for i in range (len(x)):
            y *= int(x[i])
        r += 1
        n = y
    return r
print(persistence(39))
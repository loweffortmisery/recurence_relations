def f(n = -1):
    i = 0
    while i != n:
        i += 1
        b_n = 4*i + 2
        y_n = b_n
        for j in range(2, i+1):
            b_n -= 4
            y_n = b_n + 1/y_n
        F_n = 2 + 1/y_n
        yield F_n, i



if __name__ == '__main__':
    for F, i in f(10):
        print(F,i)



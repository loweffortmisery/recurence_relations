def f(n):
    b_n = 4*n + 2
    y_n = b_n
    for i in range(2, n):
        b_n -= 4
        y_n = b_n + 1/y_n
    F_n = 2 + 1/y_n
    return F_n

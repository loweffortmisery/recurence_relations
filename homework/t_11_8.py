def f_a(n):
    a_n = 1
    S_n = 1
    for i in range(2, n+1):
        a_n = -a_n
        S_n += a_n * n
    return S_n

def f_b(n):
    # return 1 - 1/n
    S_n = 1/2
    for i in range(3, n+1):
        S_n += 1/((n-1)*n)
    return S_n

def f_c(n):
    a_n = 1
    S_n = 1/2
    for i in range(3, n+1):
        a_n = -a_n
        S_n += a_n * (n-1)/n
    return S_n



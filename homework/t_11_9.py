def f_a(n):
    P_n = 3/4
    for i in range(3, n+1):
        P_n *= (1 - 1 / (i**2))
    return P_n

def f_b(n):
    a_n = 1
    P_n = 1
    for i in range(2, n+1):
        a_n *= i
        P_n *= 2 + 1/a_n
    return P_n

def f_c(n):
    #return 2/(n+2)
    P_n = 2/3
    for i in range(2, n+1):
        P_n *= (i+1)/(i+2)

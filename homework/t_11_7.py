def f_a(x, k):
    x_k = x
    for i in range(1,k+1):
        x_k = (x^2)/((2*k)*(2*k+1)) * x_k
    return x_k

def f_b(x, k):
    a_k = -x
    x_k = a_k
    for i in range(2,k+1):
        a_k = -x * a_k
        x_k = a_k / k
    return x_k

def f_c(x, k):
    a_k = 1
    b_k = 1
    x_k = a_k / b_k
    for i in range(1, k+1):
        a_k = -x * a_k
        for j in range(k**2 - k + 1, k**2 + k + 1):
            b_k *= j
        x_k = a_k / b_k
    return x_k

def f_d(x, k):
    a_k = 1
    b_k = 1
    x_k = a_k/b_k
    for i in range(1, k+1):
        a_k = x * a_k
        b_k = k * b_k
        x_k = (k+1) * a_k / b_k
    return x_k





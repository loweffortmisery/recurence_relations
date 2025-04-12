def f_a(x, k = -1):
    x_k = x
    i = 0
    yield x_k, i
    while (i != k):
        i += 1
        x_k *= (x^2)/((2*i)*(2*i+1))
        yield x_k, i

def f_b(x, k = -1):
    a_k = -x
    x_k = a_k
    i = 1
    yield x_k, i
    while i != k:
        i += 1
        a_k = -x * a_k
        x_k = a_k / i
        yield x_k, i

def f_c(x, k = -1):
    a_k = 1
    b_k = 1
    x_k = a_k / b_k
    i = 0
    yield x_k, i
    while i != k:
        i += 1
        a_k = -x * a_k
        for j in range(i**2 - i + 1, i**2 + i + 1):
            b_k *= j
        x_k = a_k / b_k
        yield x_l, i

def f_d(x, k = -1):
    a_k = 1
    b_k = 1
    x_k = a_k/b_k
    i = 0
    yield x_k, i
    while i != k:
        i += 1
        a_k = x * a_k
        b_k = k * b_k
        x_k = (i+1) * a_k / b_k
        yield x_k, i
 





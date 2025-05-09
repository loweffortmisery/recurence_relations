def f_a(n = -1):
    P_n = 3/4
    i = 2
    yield P_n, i
    while i != n:
        i += 1
        P_n *= (1 - 1 / (i**2))

def f_b(n = -1):
    a_n = 1
    P_n = 1
    i = 1
    yield P_n, i
    while i != n:
        i += 1
        a_n *= i
        P_n *= 2 + 1/a_n
        yield P_n, i

def f_c(n = -1):
    #return 2/(n+2)
    P_n = 2/3
    i = 1
    yield P_n, i
    while i != n:
        i += 1
        P_n *= (i+1)/(i+2)
        yield P_n, i



if __name__ == '__main__':
    print("(a):")
    for P, i in f_a(10):
        print(P,i)
    print("\n\n(b):")
    for P, i in f_b(10):
        print(P,i)
    print("\n\n(c):")
    for P, i in f_c(10):
        print(P,i)



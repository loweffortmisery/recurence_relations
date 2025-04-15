def f_a(n = -1):
    a_n = 1
    S_n = 1
    i = 1
    yield S_n, i
    while(i != n):
        i += 1
        a_n = -a_n
        S_n += a_n * i
        yield S_n, i

def f_b(n = -1):
    # return 1 - 1/n
    S_n = 1/2
    i = 2
    yield S_n, i
    while(i != n):
        i += 1
        S_n += 1/((i-1)*i)
        yield S_n, i

def f_c(n = -1):
    a_n = 1
    S_n = 1/2
    i = 2
    yield S_n, i
    while(i != n):
        i += 1
        a_n = -a_n
        S_n += a_n * (i-1)/i
        yield S_n, i


if __name__ == '__main__':
    print("(a):")
    for S, i in f_a(10):
        print(S,i)
    print("\n\n(b):")
    for S, i in f_b(10):
        print(S,i)
    print("\n\n(c):")
    for S, i in f_c(10):
        print(S,i)



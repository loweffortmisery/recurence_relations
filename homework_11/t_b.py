def P_n(n=-1):
    P = 2
    k = 1
    yield P, k
    while k != n:
        k += 1
        P *= (1 + 1 / (k ** 2))
        yield P, k

if __name__ == "__main__":
    for P, k in P_n(3):  
        print(f"P_{k} = {P}")

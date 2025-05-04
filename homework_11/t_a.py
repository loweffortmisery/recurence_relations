

def X_k(x, n=-1):
    a_k = 1
    k = 0
    x_k = 1
    x_pow2 = x*x
    yield x_k, k
    while (k != n):
        k += 1
        a_k *= (2*k * (2*k - 1))
        x_k = x_k * x_pow2 / a_k 
        yield x_k, k
        

if __name__ == "__main__":
    for x_k, k in X_k(2, 3):
        print(f"x_{k} = {x_k}\n")

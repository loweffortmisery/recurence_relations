import math

def f(x, e = 1e-10):
    r = 2*x
    last = r
    k = 0
    x_k = x
    x_pow2 = x*x
    a_k = 1 #2*k+1
#    yield r,k
    while(last > e):
        #k += 1
        a_k += 2
        x_k *= x_pow2
        last = 2*x_k/a_k
        r += last
 #       yield r,k
    return r

if __name__ == "__main__":
    x = 0.5
    print(f"by function:\n ln((1+{x})/(1-{x})) = {f(x)}\nby math:\n{math.log((1+x)/(1-x))}\n")


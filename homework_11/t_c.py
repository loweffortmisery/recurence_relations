def det_A_n(a,b,n=-1):
    d1 = a+b
    d2 = (a+b)**2 - a*b
    d3 = (a+b)*d2 - a*b*(d1)
    k = 1
    yield d1, k
    while(k != n):
        k+=1
        d1, d2, d3 = d2, d3, (a+b)*d2 - a*b*d1
        yield d1, k

if __name__ == "__main__":
    for D, k in det_A_n(2,5,n=4):
        print(f"det(A(2,5)_{k}) = {D}\n")

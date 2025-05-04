def S_n(n=-1):
    a1 = a2 = a3 = 1
    k = 1
    b_k = 2
    S = 1/2
    yield S, k
    
    while(n!=k):
        k+=1
        a1,a2,a3 = a2,a3,a3-a1
        b_k *= 2
        S += a1/b_k
        yield S, k

if __name__ == "__main__":
    for S, k in S_n(5):
        print(f"S_{k} = {S}\n")

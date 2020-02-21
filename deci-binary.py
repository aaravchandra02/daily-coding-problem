def generate_pseudo_binary(n):
    l_n = len(str(n))
    tl = [0,1]
    for i in range(1,l_n):
        cc = 10**i
        [tl.append(cc + tl[j]) for j in range(len(tl))]  
    return(tl)


def soln(n):
    l = generate_pseudo_binary(n)
    print(l)
    l = l[::-1]
    res = []
    for i in l:
        while(n>=i and n>0):
            n=n-i
            res.append(i)          
    print(res,sum(res))

soln(6543219)



        


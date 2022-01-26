def printseries(a):
    ith_term=0
    for i in range(1, a+1):
        ith_term=(13*i*(i-1))/2+2
        print(int(ith_term),",",end="")
if __name__=="__main__":
    a=int(input("Enter no. of terms to be printed= "))
    printseries(a)

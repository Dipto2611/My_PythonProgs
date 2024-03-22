def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=0
        b=1
        for i in range(1,n): 
            c=a+b
            a=b
            b=c
        return b
for i in range(0,11):
    print("Fibbonaci of",i,"is",fibo(i))


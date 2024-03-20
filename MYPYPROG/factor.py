n=int(input("Enter a no:"))
def factors(n):
    flist=[]
    for i in range(1,n+1):
        if n%i==0:
            flist.append(i)

    print(flist)

factors(n)

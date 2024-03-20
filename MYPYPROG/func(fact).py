#to find fact usinf func
def findfact(num):
    fact = 1
    i = 1 
    while i <= num:
        fact *= i
        i += 1
    return fact

num = int(input("Enter a number: "))
print(findfact(num))

####################################################

#to calc usd to inr

def usdtoinr(val):
    return val* 83    

val=int(input("enter a no:"))
print(usdtoinr(val))

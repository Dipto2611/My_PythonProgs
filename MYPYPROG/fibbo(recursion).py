def fibo(n):
   if n==0: 
      return 0
   elif  n==1:
        return 1
   else:
      return fibo(n-1)+fibo(n-2)
   
for i in range(0,11):
   print("Fibbonaci of",i,"th","is",fibo(i))



#######################################################

#  MEMOIZATION PROCESS    (Also this is a process for searching no at particular pos)

fibtable = {}

def fib(n):
    if n in fibtable:
        return fibtable[n]
    if n == 0 or n == 1:
        value = n
    else:
        value = fib(n-1) + fib(n-2)
    fibtable[n] = value 
    return value

# Take user input for the value of n
num = int(input("Enter the value of num: "))

# Calculate and print the nth Fibonacci number
print("Fibonacci number at position", num, "is", fib(num))

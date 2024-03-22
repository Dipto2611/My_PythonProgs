#to find fact using func

def findfact(num):
    fact = 1
    i = 1 
    while i <= num:
        fact *= i
        i += 1
    return fact

num = int(input("Enter a number: "))
print(findfact(num))

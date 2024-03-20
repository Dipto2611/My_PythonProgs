# #find fact by recur

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
    
# n=int(input("enter no:"))
# print(fact(n))
# print("The fact of",n ,"is",fact(n))



#find sum of first n natural no

def sum(n):
    if(n==0):
      return 0
    else:
        return n + sum(n-1)

n=int(input("enter no:"))
print(sum(n))
print("The sum of",n ,"is",sum(n))
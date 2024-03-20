#find sum using while
n=int(input("Enter no:"))
sum=0
i = 1
while i <= n:
    sum += i
    i=i+1
print("total sum =",sum)


#for loop

n=5
sum=0
for i in range(1,n+1):
    sum+=i

print("total sum",sum)
#search X el in list/tup using for loop

tup= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36, 11, 36)

x=49
# pos=1
for items in range(len(tup)):
    if(tup[items]==x):
        print("Found at",items+1)
    # pos+=1                               #to find position/traverse



###################################################################################



#print Search for a number X in this tuple using loop:

tup= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x=49   #int(input("Enter a no:"))

i=0
while i<len(tup):  #whenevr "<=" sign thn -1 is must otherwise, < dene se -1 nhi lagta
    if(tup[i]==x):
        print("Match found at index",i )
    i+=1


#########################################################
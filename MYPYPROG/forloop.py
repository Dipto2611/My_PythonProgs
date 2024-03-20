#search X el in list/tup using for loop

tup= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36, 11, 36)

x=49
# pos=1
for items in range(len(tup)):
    if(tup[items]==x):
        print("Found at",items+1)
    # pos+=1                               #to find position/traverse

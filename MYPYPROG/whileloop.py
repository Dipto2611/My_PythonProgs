# #1 to 100 print
# i=1
# while i<=100:
#     print(i)
#     i+=1

# print("LOOP ENDED")

# #########################################################

# #100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1
# print("done")

# #########################################################


# #print table 
# i=1
# while i<=10:
#     print("2 x",i,"=",2*i)
#     i+=1

# print("Table done")

# #########################################################

# #print the list from 1 to 10 sq.

# list=[1,4,9,16,25,36,49,64,81,100]
# index=0  #as index starts from 0 and here 10 nos are therefore we've to call it to 9 

# while index<len(list):
#     print(list[index])
#     index+=1            #update imp*


# #########################################################
    



#print Search for a number X in this tuple using loop:

tup= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x=int(input("Enter a no:"))

i=0
while i<len(tup):  #whenevr "<=" sign thn -1 is must otherwise, < dene se -1 nhi lagta
    if(tup[i]==x):
        print("Match found at index",i )
    i+=1


#########################################################
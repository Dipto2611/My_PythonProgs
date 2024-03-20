#binary search

def binary_search(key,arr):
    i =0
    j =len(arr)
    flag =0

   #implementation 
    while i<j and flag == 0:
       
        midpt=(i + j)//2  #1st check out this
       
        if arr[midpt] == key:
            pos=midpt+1
            flag=1
        elif arr[midpt]>key:
            j=midpt-1
        else:
            i=midpt+1

    if flag == 1:
        print("Position found at",pos)
    else:
        print("Not found")

arr = [11, 3, 45, 25, 75, 23, 32, 1]
print("Original array:",arr)
arr.sort()
print("Sorted array:",arr)

key=int(input("Enter a number you want to search:"))

binary_search(key,arr)      #dont forget to call it niggachu
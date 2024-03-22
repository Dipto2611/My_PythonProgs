def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        cur_pos=i  #assign current position to i (here 23=i)
        while arr[cur_pos-1]>arr[cur_pos] and cur_pos>0: #if left index is > than currnt pos then shift right side the element
           arr[cur_pos-1],arr[cur_pos]=arr[cur_pos],arr[cur_pos-1]
           cur_pos-=1



arr=[2,23,54,1,7,5,39,69,10,64]
insertion_sort(arr)
print(arr)



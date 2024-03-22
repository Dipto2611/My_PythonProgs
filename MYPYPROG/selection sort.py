def selection_sort(list):
    for i in range(len(list)):   #0 to len of list
        min_index=i
        for j in range(i+1,len(list)): #here i+1 bec after considering 1st val we've to check the unsorted one so
            if list[j]<list[min_index]:
                min_index=j
        
        #swap
        list[i], list[min_index] = list[min_index], list[i]

#list[i], list[min_index] is this only l= 2,34
       


list=[2,34,55,21,8,5,3,45]
selection_sort(list)
print("Sorted array is",list)
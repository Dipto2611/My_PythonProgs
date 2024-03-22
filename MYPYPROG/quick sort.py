def quicksort(seq):
    length=len(seq)
    
    if length<=1:
        return seq
    else:
        pivot=seq.pop()  #mark the last item as center


    left_items=[] 
    right_items=[]
    
    for items in seq:
        if items < pivot:
            left_items.append(items)
        else:
            right_items.append(items)

    
    return quicksort(left_items) + [pivot] + quicksort(right_items) #recursion

seq=[27,1,3,9,6,78,20,5,14]

sorted_seq = quicksort(seq)
print("Sorted sequence is:", sorted_seq)


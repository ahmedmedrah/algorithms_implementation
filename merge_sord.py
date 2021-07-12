def merge(left,right):
    arr = []
    i = j = 0
    # merge until one side is done
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    # see if any side still have elements in it
    while i < len(left):
        arr.append(left[i])
        i+=1
    
    while j < len(right):
        arr.append(right[j])  
        j+=1

    return arr

def merge_sort(A):
    # base case is when A is only one element
    if len(A) == 1:
        return A
    else:
        # get the mid index
        mid = len(A) // 2
        # sort left and right side recursivly
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        # merge the 2 sides
        sol = merge(left,right)
        return sol
M = [6,1,2,5,3,9,7,10,99,16,19]
sorted_M = merge_sort(M)
print('before',M)
print('after',sorted_M)
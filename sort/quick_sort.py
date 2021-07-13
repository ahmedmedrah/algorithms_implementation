def quicksort(arr):
    if len(arr) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return arr
    else:
        # recursive case
        mid = len(arr)//2
        pivot = arr[mid]
        # sub-array of all the elements less than the pivot
        less = [i for i in arr if i < pivot]
        # sub-array of all the elements same as the pivot
        same = [i for i in arr if i == pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in arr if i > pivot]
        print(mid)
        return quicksort(less) + same + quicksort(greater)

A = [7,9,5,3,1,3,4,6,1,0,-1,20] 
z = quicksort(A)
print(z)
## iterative method
def binary_search(m,e):
    steps = 0
    low = 0
    high = len(m)-1
    mid = (low + high) // 2
    while low <= high:
        steps += 1
        if e == m[mid]:
            return mid
        elif e > m[mid]:
            low = mid + 1
            mid = (low + high) // 2
        else:
            high = mid - 1
            mid = (low + high) // 2
    return -1

A = [0,1,3,5,6,8,10,11]
print(binary_search(A,3))



## recursion method
def rec_bin_search(arr,l,h,e):    
    m = (l + h)//2
    if arr[m] == e:
        return m
    elif arr[m] > e:
        return rec_bin_search(arr,l,m-1,e)
    elif arr[m] < e:
        return rec_bin_search(arr,m+1,h,e)
    else:
        return -1
    
rec_bin_search(A,0,len(A)-1,3)    
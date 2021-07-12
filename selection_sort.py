def selection_sort(m):
    for i in range(len(m)):
        mn = i
        for j in range(i+1,len(m)):
            if m[j] < m[mn]:
                mn = j        
        m[mn],m[i] = m[i],m[mn]
    return m    

A = [5,1,3,7,2,9,10,0]
print(selection_sort(A))
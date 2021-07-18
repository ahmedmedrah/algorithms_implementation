word1 = 'fish'
word2 = 'hish'

def longest_substring(w1,w2):
    # create an empty grid w1 length by w2 length
    grid = [[0]*len(w2) for i in range(len(w1))]
    for i in range(len(w1)):
        for j in range(len(w2)):
            # check if the letters match
            if w1[i] == w2[j]:
                # set the cell corresponding to the match to the value of the last match +1                          
                last = grid[i-1][j-1] +1
                grid[i][j] = last  
    # return the largest match            
    return max(max(grid))

print(longest_substring(word1,word2))                    
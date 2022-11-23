class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #length of text1
        m = len(text1) 
        #length of text2
        n = len(text2) 
        #list comprehension with 0 as initial values
        grid = [[0 for i in range(n+1)] for j in range(m+1)] 

        #iterate through the grid until -1 index in reverse in rowwise
        for i in range(m-1,-1,-1):
             #iterate through the grid until -1 index in reverse in columnwise
            for j in range(n-1,-1,-1):
                #if the text1 equals to text2
                if text1[i]==text2[j]:
                    grid[i][j] = 1+ grid[i+1][j+1]

                else:
                    #grid[i][j] will be the maximum value between the grid[j+1][i] and grid[i+1][j]
                    grid[i][j] += max(grid[i][j+1],grid[i+1][j]) 

#the grid starting index holds the longest common subsequence number
        return grid[0][0]
        
        
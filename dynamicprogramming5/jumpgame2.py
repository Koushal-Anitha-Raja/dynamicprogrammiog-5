class Solution:
    def jump(self, nums: List[int]) -> int:
        #assigning start as 0
        start = 0 
        #assigning end as 0
        end = 0
        #assigning jump as 0
        jumps = 0 
        
        #iterate through until lenght of nums is greater than end
        while end<len(nums)-1:
            #assign farthest as zero
            farthest = 0 
            #iterate from start to the end 
            for i in range(start,end+1): 
                #farthest will be the maximum between farthest and i+ nums of ith value
                farthest = max(farthest,i+nums[i])
            #increase jump by one
            jumps+=1
            #start to end  plus one
            start = end+1 
            #and end to farthest
            end = farthest
            #return the number of jumps
        return jumps
        
"""Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs."""



 #check for matching list member  
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_matches = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j] and i < j:# and nums.index(i) < nums.index(j):
                    num_matches +=1
        return(num_matches)


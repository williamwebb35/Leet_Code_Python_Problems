class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        all_counts = []
        for i in nums:
            count = 0
            for j in range(len(nums)):
                if i > nums[j]:
                    count +=1
            all_counts.append(count)
        return(all_counts) 

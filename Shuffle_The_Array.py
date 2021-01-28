#Given the array nums consisting of 2n elements in the form....
#... [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
    # strategy: divide length of nums by n, resulting in n new lists
        nums1 = nums[:n]
        nums2 = nums[n:]
        # try to zip the n lists together
        new_nums = zip(nums1,nums2)
        # combine the list of two-tuples into a single list
        e = []
        for i in new_nums: e.extend(list(i))   
        return(e)


 
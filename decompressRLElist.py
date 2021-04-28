"""
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0). 
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        groups = list(zip((nums[0::2]),(nums[1::2])))
        out = []
        for i in groups:
            for j in range(i[0]):
                out.append(i[1])
        return(out)

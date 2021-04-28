"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # convert to string
        numstr = str(n)
        # iterate over string with list comprehension to create list of integers
        numstrlc = [int(i) for i in numstr]
        total = 0
        product = 1
        for i in (range(len(numstrlc))):
            total += numstrlc[i]
            product *= numstrlc[i]
            difference = product - total
        return(difference)

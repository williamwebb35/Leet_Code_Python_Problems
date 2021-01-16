# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/

#1431. Kids With the Greatest Number of Candies

#Given the array candies and the integer extraCandies, where candies[i] represents ...
#....the number of candies that the ith kid has.

#For each kid check if there is a way to distribute extraCandies among the kids such ...
#...that he or she can have the greatest number of candies among them. Notice that ...
#...multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_num = max(candies) # establish the pre-existing largest number in candies
        new_num_candies =  [i + extraCandies for i in candies] # add extraCandies to each item in candies
        # check if each item in new_num_candies is greater than or equal to greatest_num
        check_greatest = [ i >= greatest_num for i in new_num_candies]
        #print(candies, extraCandies, greatest_num, new_num_candies, check_greatest)
        return(check_greatest)
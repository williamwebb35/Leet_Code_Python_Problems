#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # reverse the order of each list
        # combine each list into a single number
        # add both resulting numbers 
        
        #l1 = [2,4,3]
        #l2 = [5,6,4]
        rev_l1 = list(reversed(l1))
        rev_l2 = list(reversed(l2))
        #print(rev_l1,rev_l2)
        newl1 = int(''.join([str(x) for x in rev_l1]))
        newl2 = int(''.join([str(x) for x in rev_l2]))
        newl3 = str(newl1+newl2)
        newl4 = []
        for i in newl3:
            newl4.append(i)
        newl5 = list(reversed(newl4))
        newl6 = []
        for i in newl5:
            newl6.append(int(i))
        print(newl6)
        return(newl6)
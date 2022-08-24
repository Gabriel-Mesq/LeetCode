#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # convert it into a normal list
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next
            
        # check for palindrome
        if ls == ls[::-1]:
            return True
        else: 
            return False
        
# @lc code=end


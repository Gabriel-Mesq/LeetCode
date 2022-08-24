#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):

        aux = x
        reversed_num = 0

        while x != 0 and x >= 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        if aux == reversed_num:
            return True
        
        else: return False

# @lc code=end


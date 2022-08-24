#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()
        
        i = 1
        
        for num in nums:
        
            if num == i:
                i += 1
        
        return i
        
# @lc code=end


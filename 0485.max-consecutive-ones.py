#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ct = 0
        max = 0

        for i in range(len(nums)):
            
            if nums[i] == 1:
                
                ct += 1

                if ct > max:
                    max = ct

            else: ct = 0

        return max

# @lc code=end


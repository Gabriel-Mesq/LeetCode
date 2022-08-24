#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
from operator import length_hint


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums) + 1
        nums = set(nums)
        r = []
        
        for i in range(1, n):
            if i not in nums:
                r.append(i)

        return r


# @lc code=end


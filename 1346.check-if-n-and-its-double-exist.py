#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, A: List[int]) -> bool:
        if A.count(0) > 1: return True
        S = set(A) - {0}
        for a in A:
            if 2*a in S: return True
        return False
		
# @lc code=end


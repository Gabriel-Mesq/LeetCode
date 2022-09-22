#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        flag = 0 
        
        for i in range(len(min(strs, key=len))):
            
            for j in range(len(strs)):
                
                if strs[0][i] != strs[j][i]:
                    flag = 1
            
            if flag == 0:
                res += strs[0][i]

        return res

# @lc code=end


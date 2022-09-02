#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = []
        maior = 0
        start = 0
        end = 0
        
        while end < len (s):
        
            if s[end] not in seen :
                seen.append(s[end])
                end +=1
                maior = max(maior, len(seen))
            
            else:
                seen.remove(s[start])
                start += 1
        
        return maior
        
# @lc code=end


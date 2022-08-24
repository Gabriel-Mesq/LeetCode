#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
       
        r = f = 0                 
      
        if x < 0:
            x = x*-1
            f = 1
        
        while x != 0:
            u = x % 10
            r = r*10 + u
            x //= 10

        if (r < -2147483648 or r > 2147483647):
            return 0

        if f == 1:
            return r*-1

        return r

# @lc code=end


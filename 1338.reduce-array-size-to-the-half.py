#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#

# @lc code=start
#Ideia: reduzir numero mais popular, checar len <= 50%, repetir. 

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        
        for index, count in enumerate(sorted(collections.Counter(arr).values(), reverse=True)):
            total_count += count
            
            if total_count >= len(arr) // 2:
                return index + 1
        
        return 0
                
# @lc code=end

